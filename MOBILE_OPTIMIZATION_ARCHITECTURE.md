# Flip Runner: Mobile Optimization & UI/UX Architecture

**Role**: Lead Mobile Optimization Engineer & UI/UX Architect

This document outlines the rigorous technical standards and architectural patterns required to execute flawless mobile optimization for iOS and Android in *Flip Runner*. To guarantee competitive integrity in a deterministic endless runner, these guidelines govern UI architecture, input precision, memory management, and lifecycle safety.

---

## 1. Responsive UI Architecture and Safe Zones

To achieve flawless presentation across all modern mobile form factors (from 4:3 iPads to 19.5:9 Samsung/iPhone ultrawides), we must utilize a deterministic mathematical framework for canvas scaling and anchoring, completely decoupled from physical pixel dimensions.

### 1.1 Mathematical Framework for Canvas Scaling
We employ a **Reference Resolution** strategy (e.g., 1920x1080) utilizing a **Scale with Screen Size** approach via a specific match algorithm.
*   **Match Factor**: Let $W_r, H_r$ be the reference width and height. Let $W_s, H_s$ be the screen width and height.
*   The scale factor $S$ is calculated based on a match coefficient $m \in [0, 1]$ (where 0 matches width, 1 matches height):
    $S = (W_s / W_r)^{1-m} \times (H_s / H_r)^m$
*   For a 2D endless runner where vertical physics constraints are strictly controlled and horizontal anticipation is key, we enforce a fixed vertical scale ($m = 1$). This ensures the vertical physics coordinate space remains mathematically constant across devices, while granting ultrawide devices extra peripheral vision without altering core gameplay logic.

### 1.2 Dynamic "Safe Area" Calculations
Notches, dynamic islands, and physical bezels must never occlude interactive UI elements or critical gameplay warnings.
*   **Hardware Polling**: At boot and on dimension change events, we poll the OS for Safe Area Insets (Top, Bottom, Left, Right) via native APIs (e.g., `WindowInsets` on Android, `safeAreaInsets` on iOS).
*   **Logical Safe Rect**: The UI root canvas calculates a `LogicalSafeRect`:
    *   `Width = Screen Width - (Inset.Left + Inset.Right)`
    *   `Height = Screen Height - (Inset.Top + Inset.Bottom)`
*   **Anchoring System**: UI widgets use 9-slice anchoring mapped exclusively to the `LogicalSafeRect`, not the physical screen rect. 
    *   *Example*: The pause button is anchored to `Top-Right` of the `LogicalSafeRect` with a static 30pt offset, guaranteeing it sits exactly 30pt from the hardware occlusion, preserving structural consistency regardless of the hardware's bezel design.

---

## 2. Frame-Perfect Touch Input Validation

In a deterministic physics environment requiring frame-perfect maneuvers, variable input latency destroys competitive integrity. The architecture must strictly decouple hardware input polling from visual rendering and physics steps.

### 2.1 Decoupled Input Architecture
*   **Raw Input Buffer**: We implement an immediate-mode input buffer. Native touch events from the OS level interrupt the main thread and write immediately to a highly-optimized ring buffer: `Struct TouchEvent { timestamp, state, touch_id, x, y }`.
*   **Deterministic Physics Consumption**: The physics loop runs on a Fixed Timestep (e.g., 0.0166s for a 60Hz tick rate). At the beginning of each tick, the engine drains the input buffer, applying inputs based on their *precise hardware timestamp*. We interpolate sub-tick physics logic to maintain exact jump apexes regardless of render frame variances or dropped render frames.

### 2.2 Hitbox Scaling and Physical Tolerances
*   **Physical Millimeters to Points**: Pixels are arbitrary for measuring ergonomics. We calculate the device DPI/PPI on load. A minimum interactive tap target must be mathematically guaranteed to be at least **7mm x 7mm** on the physical glass (approx 44x44 points at 160ppi).
*   **Conversion Math**: `TargetPixels = (TargetMM / 25.4) * DevicePPI`. UI hitboxes scale dynamically based on this calculation, completely independent of the canvas reference scale.

### 2.3 Multi-Touch Edge-Case Handling
*   **Heuristic Priority Masking**: When polling for an "Action" (e.g., Jump/Ability), we use a priority mask. If the screen is receiving a swipe (deltas over time exceeding a threshold), that touch index is flagged as `CONSUMED_BY_GESTURE` and ignored by the tap-listener logic.
*   **Palm Rejection & Edge Protection**: Touches originating within the outermost 5% of the screen edges without moving inward are filtered via a delayed-activation heuristic. This prevents accidental palms gripping the device from triggering abilities or eating input limits.

---

## 3. Performance Profiling and Memory Management

A locked 60 FPS (with 120 FPS support) target means we have ~16.6ms or ~8.3ms per frame respectively. Thermal throttling is the silent killer of mobile performance. Our CPU/GPU budget must be heavily optimized for low power consumption to prevent device downclocking during extended sessions.

### 3.1 Object Pooling Pipeline
*   **Zero Allocation Rule**: Instantiating (`new`) or Destroying (`delete`) objects during active gameplay causes unpredictable Garbage Collection (GC) spikes, resulting in micro-stutters.
*   **Pre-Allocation**: During the loading screen, we pre-allocate deterministic pools for all dynamic entities (Particles, Obstacles, Coins, Projectiles). 
*   **Pool Management**: We use tightly packed contiguous arrays to guarantee memory locality. When an object "dies", it is deactivated (flags toggled, removed from render queue) and added to a `FreeList` stack for $O(1)$ retrieval without allocation.

### 3.2 Texture Compression and VRAM
*   **Hardware-Native Formats**: We strictly avoid uncompressed (PNG/JPG) assets in VRAM. All assets are baked offline into hardware-compressed formats: **ASTC (Adaptive Scalable Texture Compression)** for optimal iOS/Android cross-compatibility, leveraging block footprints that balance quality and file size.
*   **Draw Call Reduction**: UI atlases are aggressively packed. We batch render calls by material and disable anisotropic filtering for 2D sprites. Mip-map generation is strictly controlled to save memory bandwidth.

### 3.3 Garbage Collection Avoidance
*   **Structs over Classes**: In C#/C++ environments, we aggressively utilize value types (structs) passed by reference to avoid heap allocations entirely.
*   **String Interning**: UI text updates (e.g., the Score counter ticking up every frame) use pre-allocated character arrays or optimized string builders. We NEVER concatenate primitive strings during gameplay (e.g., `score.ToString() + "!"`), as this creates massive amounts of transient heap garbage.

---

## 4. Interruption and State Management

Mobile environments are highly volatile. The OS is aggressive about reclaiming resources. The interruption logic must be bulletproof to maintain player trust and never fail a run due to external factors.

### 4.1 The Interruption Logic Controller
We employ a robust Finite State Machine (FSM) hooked directly into native OS lifecycle events (`OnApplicationPause`, `OnApplicationFocus`, `applicationWillResignActive`).

*   **Impending Interruptions**: When a 10% battery warning or an incoming phone call occurs, the OS sends a "Resign Active" signal *before* the application is fully backgrounded. The engine immediately flags `IS_INTERRUPTED = true`.
*   **Immediate Pause Enforcement**: If `IS_INTERRUPTED` is detected between frames, the engine executes an atomic `ForcePause()` override. This bypasses normal UI pause transitions (e.g., tweening menus) and instantly freezes the deterministic physics tick.

### 4.2 Pause-and-Resume Serialization
If the app is aggressively backgrounded, the OS might kill the process to save RAM without warning.
*   **Tick-State Serialization**: Every few seconds (or at deterministic checkpoint milestones), the complete game state (Randomizer Seed, Current Tick Count, Entity Positions, Velocity vectors) is serialized into a lightweight byte array and written asynchronously to a secure memory-mapped file or PlayerPrefs.
*   **Resumption Protocol**: 
    1. On normal focus return, the game boots into a **Hard Paused** state featuring a mandatory "Resume" countdown (3..2..1) to prevent the player from being blindsided by immediate gameplay.
    2. If the OS killed the app entirely, on the next launch the boot sequence detects the uncompleted run file, loads the state via the serialized byte array, and transparently rebuilds the exact physics state up to the last saved tick, finally presenting the same "Resume" countdown. 
