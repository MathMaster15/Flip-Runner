# Flip Runner: Behavioral Psychology & Retention Systems
**Role:** Lead Systems Designer (Behavioral Psychology & Player Retention)
**Target:** Maximizing the Core Compulsion Loop & Long-Term Retention

This document details the behavioral frameworks, mathematical pacing, and UI/UX structures designed to optimize player retention, engagement, and the "just one more run" compulsion loop in Flip Runner.

---

## 1. Engineering the "Near-Miss"

The "near-miss" effect is a psychological phenomenon where a failure that feels *close* to success triggers the exact same dopamine pathways as an actual victory, creating an overwhelming urge to retry. In a deterministic runner, we must manufacture these scenarios structurally and visually.

### Chunk Design for Near-Misses
We design specific "choke points" within high-intensity chunks. These points require precise inputs but are highly telegraphed. 
*   **The Bait:** Place a high-value collectible (e.g., a Premium Token) on a risky trajectory that requires a late-frame jump.
*   **The Clearance:** The collision mesh of the hazard should be *slightly smaller* (e.g., 5-8% smaller) than the visual sprite. If the player clips the sprite but clears the mesh, they get a "shave" visual effect (sparks). If they fail, they know their input was demonstrably late or early.

### Failure Feedback & Blame Transfer
When the player dies, the game must instantly communicate that the system is fair and the failure was 100% their fault.
*   **Visual Snapshot:** Upon death, the screen freezes for 0.5 seconds, highlighting the exact point of collision. A subtle, high-contrast outline flashes on the hazard.
*   **Input Ghosting:** Briefly display a ghosted overlay of the exact button press (or lack thereof) at the moment of failure relative to the ideal input window. 
*   **Audio Profile:** The death sound must not be mocking or overly harsh. It should be a sudden, crisp "snap" (cutting off the music track entirely), followed instantly by a low, ascending bass sweep on the retry screen, sonically pushing the player *forward* into the next run.
*   **Instant Retry:** The transition from the death screen to a new run must be frictionless (under 0.3 seconds). No loading screens.

---

## 2. Variable Ratio Reward Structures

A fixed reward structure (e.g., exactly 10 coins per run) leads to habituation and boredom. A variable ratio structure (like a slot machine) is highly compelling but can inflate the economy if unchecked. We implement a **Weighted Loot Table with Pity Timers**.

### The Distribution Model
End-of-run rewards (Loot Boxes/Chests) yield values based on a controlled probability matrix, rather than a raw random number generator (RNG).

**Loot Table (Example Chest):**
*   **Common (70%):** 50 Coins, 5 XP (The Baseline)
*   **Uncommon (20%):** 100 Coins, 15 XP
*   **Rare (8%):** 500 Coins, 1 Gem
*   **Legendary (2%):** 2500 Coins, 5 Gems, 1 Premium Token (The Dopamine Hit)

### Economy Control via Pity Timers (Pseudo-RNG)
To ensure the economy does not inflate through sheer luck, and to protect players from extreme bad luck, we use a Pseudo-RNG model.
*   Each time a player fails to roll a Legendary, the probability of rolling one in the next chest increases by a small scalar (e.g., +0.5%).
*   Once a Legendary is rolled, the probability hard-resets to the base 2%.
*   **Mathematical Safety:** We calculate the Expected Value (EV) of the chest over 100 pulls taking the pity timer into account. The overall economy balancing uses this precise EV, ensuring the "rare hits" are budgeted into the F2P progression curve.

---

## 3. The Overlapping Goal Matrix

To trigger the "just one more run" compulsion, the player must *never* have a completely clean slate. At the end of every 2-minute session, they must be agonizingly close to completing at least one objective.

### Pacing the Matrix
We track three tiers of goals simultaneously:
1.  **Micro (Session-based):** "Collect 500 coins," "Perform 10 perfect jumps." (Completes in 1-3 runs).
2.  **Meso (Daily/Weekly):** "Run 10,000 meters total," "Unlock a Tier 2 Upgrade." (Completes in 3-7 days).
3.  **Macro (Lifetime):** "Reach Player Level 50," "Unlock the Golden Avatar." (Completes in 1-3 months).

### The Statistical Guarantee (The 80-95% Rule)
The system actively manipulates the selection of Micro goals.
*   **Dynamic Goal Injector:** The game queries the player's average stats. If the player averages 200 coins per run, the system issues a "Collect 550 coins" Micro goal. 
*   After two average runs (400 coins), the player is at ~72% completion. They are statistically highly likely to hit 90%+ on the *third* run. 
*   **UI Presentation:** On the post-run death screen, the progress bar for the closest goal is always displayed front and center. The bar actively animates filling up, stopping at 85-95%. A pulsating "Retry" button is placed immediately below this nearly complete bar.

---

## 4. Loss Aversion and Sunk Cost Mechanics

Humans feel the pain of losing something roughly twice as powerfully as the pleasure of gaining it. We utilize this ethically to drive daily Active Users (DAU).

### The Daily Streak Engine
Rather than a simple "Log in 7 days for a big reward," the streak must have tangible, escalating stakes that are visible from Day 1.
*   **The Setup:** A 14-day reward calendar. Days 1-13 offer good rewards, but Day 14 offers a highly coveted, exclusive cosmetic or massive currency drop.
*   **The Loss Condition:** If a player misses a day, the streak does not reset to zero. Instead, it "cracks." A cracked streak prevents claiming the Day 14 reward.
*   **The Ethical Recovery:** To prevent ultimate burnout (which causes permanent churn if a 13-day streak is lost), players can "repair" a cracked streak. This costs a premium currency (Gems) or requires watching an ad. This turns the loss aversion into a monetization/engagement sink without hard-locking the player out of their sunk cost.

### The Runner Pass (Battle Pass)
The Runner Pass features a Free Track and a Premium Track.
*   **The Banked Reward Mechanism:** As F2P players progress, they unlock the Free rewards, but they also visibly *see* the Premium rewards they have "already earned" being banked into a locked vault. 
*   By the end of the season, the UI emphasizes: *"You have 5,000 Coins, 50 Gems, and 3 Exclusive Skins waiting for you in the vault."* The sunk cost of their time investment heavily incentivizes converting to a paid user just before the season expires so they don't "lose" the items they spent weeks grinding past.
