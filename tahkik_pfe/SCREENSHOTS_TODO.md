# Screenshots TODO — Tahkik Platform

All old screenshots have been deleted. You need to capture **18 screens total** (15 dashboard + 3 mobile) and save them into the `picture/` folder of this LaTeX project.

When you finish, ping me and I'll wire each `picture/<filename>.png` into the right `\screenshotplaceholder{...}` slot in `chapters/chapter3_implementation.tex`.

---

## How to capture

### Web dashboard (15 screens)

1. In the dashboard folder, install + run:
   ```powershell
   cd D:\PFE\tahkik_dashboard-main
   npm install
   npm run dev
   ```
2. Open `http://localhost:5173` and log in as an **admin** to capture admin pages, then log out and log in as a **teacher** to capture teacher pages.
3. Capture each screen at a **wide viewport** (≥ 1440 px) so the layout looks the same as in production.
4. Save the screenshot as PNG with the exact filename below into `D:\PFE\PFE-L3-Tahkik-main\tahkik_pfe\picture\`.

### Mobile app (3 screens)

1. In the Flutter project, run on an emulator or real device:
   ```powershell
   cd D:\PFE\tahkik-app-master
   flutter pub get
   flutter run
   ```
2. Take a screenshot of each required screen (use the emulator's camera button or Android Studio's screenshot tool).
3. Crop to the device frame (no host OS chrome) and save with the exact filename into the same `picture/` folder.

---

## Required screenshots (18 total)

### Mobile app (3)

| # | Filename | App route | What to show |
|---|----------|-----------|--------------|
| 1 | `screen_login.png` | Login screen | Email / password fields + Google sign-in button on a phone-sized frame |
| 2 | `screen_signup.png` | Sign-up screen | Email / password / name fields + create-account CTA on a phone-sized frame |
| 3 | `screen_onboarding.png` | Onboarding | Recitation preferences setup (riwaya choice, daily goal, etc.) |

### Dashboard — Authentication (1)

| # | Filename | Route | What to show |
|---|----------|-------|--------------|
| 4 | `dash_login.png` | `/login` | Login card with email/password inputs and the Google Sign-In button |

### Dashboard — Admin Workspace (7)

| # | Filename | Route | What to show |
|---|----------|-------|--------------|
| 5  | `dash_overview.png` | `/admin/overview` | "Good morning, Administrator" header + 4 stat cards + usage trend + tier donut + recent submissions |
| 6  | `dash_users.png` | `/admin/users` | User Management table (name / email / role / plan / joined / status) with search input |
| 7  | `dash_teachers.png` | `/admin/teachers` | Teachers list with "+ Add Teacher" button visible at the top right |
| 8  | `dash_subscriptions.png` | `/admin/subscriptions` | Free / Premium tier cards side-by-side with user counts and feature lists |
| 9  | `dash_ai_health.png` | `/admin/ai-health` | Live health page — top banner (ok/degraded/critical) + host metrics (CPU, memory, disk, swap) + inference latency + container statuses. **Make sure `VITE_TAHKIK_SERVER_URL` is set so the live data appears.** |
| 10 | `dash_analytics.png` | `/admin/analytics` | 4 stat cards (Total Minutes, Certs, Active Teachers, Most Practiced) + 30-day usage line chart |
| 11 | `dash_daily_verse.png` | `/admin/daily-verse` | Active verse card on top + the create form + the history list of previous verses |

### Dashboard — Teacher Workspace (5)

| # | Filename | Route | What to show |
|---|----------|-------|--------------|
| 12 | `dash_teacher_overview.png` | `/teacher/overview` | Arabic greeting + 4 stat cards (Assigned Students, Recent Sessions, Certs, Avg Score) + recent recitations feed |
| 13 | `dash_students.png` | `/teacher/students/<id>` | Two-column layout — student list on the left, selected student's detail card on the right (avatar, last surah, streak, average score progress bar) |
| 14 | `dash_recitation_review.png` | `/teacher/recitation/<id>` | Submission list on the left + audio player + transcription + tajweed annotations panel on the right |
| 15 | `dash_ijaza.png` | `/teacher/ijaza` | Issue-certificate form (student / surah / riwaya / notes) + list of previously issued certificates |
| 16 | `dash_ijaza_certificate.png` | `/teacher/ijaza/<certId>` | Printable certificate detail page with student name, teacher name, surah, riwaya, and issue date |
| 17 | `dash_messages.png` | `/teacher/messages/<studentId>` | Two-column chat — student list on the left, conversation thread on the right with composer at the bottom |

### Optional (bonus)

| # | Filename | What to show |
|---|----------|--------------|
| 18 | `dash_add_teacher.png` | AddTeacher dialog open over the Teachers page |

---

## Naming rules

- All filenames use **snake_case**.
- Mobile screens use the `screen_` prefix; dashboard screens use the `dash_` prefix.
- All files go into `picture/` (the LaTeX still references `figures/` — I will copy/rename them into `figures/` once you signal "ready").
- PNG format only. JPEG is OK but rename the extension to `.png` is **not** OK — re-export properly if you only have JPG.

---

## What I will do once screenshots are ready

When you tell me the screenshots are dropped in `picture/`, I will:

1. Copy each `picture/dash_*.png` into `figures/` (so LaTeX paths stay consistent with mobile screens already there).
2. Replace each `\screenshotplaceholder{...}` in `chapters/chapter3_implementation.tex` with a proper `\includegraphics` + `\caption` + `\label`.
3. Run a sanity scan to confirm all referenced files exist before compilation.

---

## Status

### Mobile
- [ ] `screen_login.png`
- [ ] `screen_signup.png`
- [ ] `screen_onboarding.png`

### Dashboard
- [ ] `dash_login.png`
- [ ] `dash_overview.png`
- [ ] `dash_users.png`
- [ ] `dash_teachers.png`
- [ ] `dash_subscriptions.png`
- [ ] `dash_ai_health.png`
- [ ] `dash_analytics.png`
- [ ] `dash_daily_verse.png`
- [ ] `dash_teacher_overview.png`
- [ ] `dash_students.png`
- [ ] `dash_recitation_review.png`
- [ ] `dash_ijaza.png`
- [ ] `dash_ijaza_certificate.png`
- [ ] `dash_messages.png`
- [ ] `dash_add_teacher.png` *(optional)*
