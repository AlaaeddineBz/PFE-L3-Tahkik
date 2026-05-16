#!/usr/bin/env python3
"""Generate all UML diagrams for the Tahkik PFE using PlantUML web service."""

import plantuml
import os

SERVER = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/img/')
OUT = os.path.join(os.path.dirname(__file__), '..', 'tahkik_pfe', 'figures')

SKIN = """
skinparam backgroundColor white
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 13
skinparam shadowing false
skinparam roundcorner 8

skinparam usecase {
  BackgroundColor #e0f7f3
  BorderColor #0d9488
  FontColor #1e293b
  ArrowColor #0d9488
  StereotypeFontColor #0d9488
}
skinparam actor {
  BackgroundColor #0d9488
  BorderColor #0d9488
  FontColor #1e293b
}
skinparam rectangle {
  BackgroundColor #fffbeb
  BorderColor #d4af37
  FontColor #1e293b
}
skinparam sequence {
  ArrowColor #0d9488
  LifeLineBorderColor #0d9488
  LifeLineBackgroundColor #f0fdfa
  ParticipantBackgroundColor #0d9488
  ParticipantFontColor white
  ParticipantBorderColor #0d9488
  ActorBorderColor #0d9488
  ActorBackgroundColor #0d9488
  BoxBackgroundColor #fffbeb
  BoxBorderColor #d4af37
  GroupBackgroundColor #f0f9ff
  GroupBorderColor #2563eb
  DividerBackgroundColor #f0f9ff
  DividerBorderColor #64748b
}
skinparam class {
  BackgroundColor #e0f7f3
  BorderColor #0d9488
  HeaderBackgroundColor #0d9488
  FontColor #1e293b
  AttributeFontColor #1e293b
  ArrowColor #0d9488
  StereotypeFontColor white
}
skinparam note {
  BackgroundColor #fffbeb
  BorderColor #d4af37
}
skinparam package {
  BackgroundColor #fffbeb
  BorderColor #d4af37
}
skinparam component {
  BackgroundColor #e0f7f3
  BorderColor #0d9488
}
skinparam database {
  BackgroundColor #e0f7f3
  BorderColor #0d9488
}
skinparam node {
  BackgroundColor #fffbeb
  BorderColor #d4af37
}
skinparam cloud {
  BackgroundColor #f0f9ff
  BorderColor #2563eb
}
skinparam artifact {
  BackgroundColor #e0f7f3
  BorderColor #0d9488
}
"""

DIAGRAMS = {}

# ─── 1. GLOBAL USE CASE DIAGRAM ─────────────────────────────────────────
DIAGRAMS['use_case_diagram'] = SKIN + """
left to right direction
title Global Use Case Diagram — Tahkik Platform

actor "Visitor" as V
actor "Learner" as L
actor "Teacher" as T
actor "Admin" as A
actor "Tahkik AI Server" as AI
actor "Supabase" as SB

rectangle "Tahkik Platform" {
  (Sign up) as UC1
  (Forgot Password) as UC2
  (Log in) as UC3
  (Log out) as UC4
  (Browse Quran) as UC5
  (Record Recitation) as UC6
  (Get AI Feedback) as UC7
  (View Score & Errors) as UC8
  (Track Progress) as UC9
  (Manage Subscription) as UC10
  (Review Recitations) as UC11
  (Add Manual Feedback) as UC12
  (Manage Students) as UC13
  (Issue Ijaza) as UC14
  (Send Messages) as UC15
  (Manage Users) as UC16
  (Manage Teachers) as UC17
  (View Analytics) as UC18
  (Monitor AI Health) as UC19
  (Manage Subscriptions) as UC20
  (Manage Daily Verse) as UC21
}

V --> UC1
V --> UC2
L --> UC3
L --> UC4
L --> UC5
L --> UC6
L --> UC9
L --> UC10
T --> UC3
T --> UC4
T --> UC11
T --> UC13
T --> UC14
T --> UC15
A --> UC3
A --> UC4
A --> UC16
A --> UC17
A --> UC18
A --> UC19
A --> UC20
A --> UC21

UC6 ..> UC7 : <<include>>
UC7 ..> UC8 : <<include>>
UC11 ..> UC12 : <<include>>

AI --> UC7
SB --> UC3
SB --> UC1
"""

# ─── 2. RECITATION UCD ──────────────────────────────────────────────────
DIAGRAMS['ucd_recitation'] = SKIN + """
left to right direction
title Use Case Diagram — Quran Recitation and AI Feedback

actor "Learner" as L
actor "Tahkik AI Server" as AI

rectangle "Quran Recitation and AI Feedback" {
  (Browse Quran) as UC1
  (Select Surah\\nand Ayahs) as UC2
  (Record Recitation) as UC3
  (Stream Audio\\nvia WebSocket) as UC4
  (Get AI Feedback) as UC5
  (View Score\\nand Errors) as UC6
}

L --> UC1
L --> UC2
L --> UC3
AI --> UC5

UC2 ..> UC3 : <<include>>
UC3 ..> UC4 : <<include>>
UC4 ..> UC5 : <<include>>
UC5 ..> UC6 : <<include>>
"""

# ─── 3. TEACHER UCD ─────────────────────────────────────────────────────
DIAGRAMS['ucd_teacher'] = SKIN + """
left to right direction
title Use Case Diagram — Teacher Review and Student Management

actor "Teacher" as T
actor "Supabase DB" as SB

rectangle "Teacher Functionalities" {
  (Review Recitations) as UC1
  (Listen to Audio) as UC2
  (View AI Feedback) as UC3
  (Add Manual Feedback) as UC4
  (Manage Students) as UC5
  (View Student Progress) as UC6
  (Issue Ijaza Certificate) as UC7
  (Send Messages) as UC8
}

T --> UC1
T --> UC5
T --> UC7
T --> UC8
SB --> UC1
SB --> UC5

UC1 ..> UC2 : <<include>>
UC1 ..> UC3 : <<include>>
UC1 ..> UC4 : <<include>>
UC5 ..> UC6 : <<include>>
"""

# ─── 4. ADMIN UCD ───────────────────────────────────────────────────────
DIAGRAMS['ucd_admin'] = SKIN + """
left to right direction
title Use Case Diagram — Administration

actor "Admin" as A
actor "Tahkik AI Server" as AI
actor "Supabase DB" as SB

rectangle "Admin Functionalities" {
  (Monitor AI Health) as UC1
  (Manage Subscriptions) as UC2
  (Manage Users) as UC3
  (Assign Roles) as UC4
  (Manage Teachers) as UC5
  (Assign Students) as UC6
  (View Platform Analytics) as UC7
  (View Recitation\\nStatistics) as UC8
  (Manage Daily Verse) as UC9
}

A --> UC1
A --> UC2
A --> UC3
A --> UC5
A --> UC7
A --> UC9
AI --> UC1
SB --> UC3
SB --> UC7

UC3 ..> UC4 : <<include>>
UC5 ..> UC6 : <<include>>
UC7 ..> UC8 : <<include>>
"""

# ─── 5. PROGRESS UCD ────────────────────────────────────────────────────
DIAGRAMS['ucd_progress'] = SKIN + """
left to right direction
title Use Case Diagram — Progress Tracking and Subscription

actor "Learner" as L
actor "Supabase DB" as SB

rectangle "Progress and Subscription" {
  (View Progress\\nDashboard) as UC1
  (View Ijaza\\nCertificates) as UC2
  (View Streak) as UC3
  (Track Daily Goal) as UC4
  (View Recitation\\nHistory) as UC5
  (View Average\\nScores) as UC6
  (Manage Subscription) as UC7
  (Upgrade to Premium) as UC8
}

L --> UC1
L --> UC7
SB --> UC1
SB --> UC7

UC1 ..> UC2 : <<include>>
UC1 ..> UC3 : <<include>>
UC1 ..> UC4 : <<include>>
UC1 ..> UC5 : <<include>>
UC1 ..> UC6 : <<include>>
UC7 ..> UC8 : <<extend>>
"""

# ─── 6. SEQUENCE: LOGIN ─────────────────────────────────────────────────
DIAGRAMS['sequence_login'] = SKIN + """
title Sequence Diagram — Login

actor "Learner" as L
participant "Tahkik App\\n(Flutter)" as App
participant "Supabase Auth" as Auth
database "Supabase DB" as DB

L -> App : Open login screen
L -> App : Enter email / password

alt Email / Password Login
  App -> Auth : signInWithEmail(email, pwd)
  Auth -> DB : Validate credentials
  DB --> Auth : User record
  Auth --> App : AuthResponse (JWT token)
else Google Sign-In
  App -> Auth : signInWithOAuth(google)
  Auth -> Auth : OAuth flow
  Auth --> App : AuthResponse (JWT token)
end

alt Success
  App --> L : Navigate to home screen
else Invalid credentials
  App --> L : Display error message
end
"""

# ─── 7. SEQUENCE: SIGN-UP ───────────────────────────────────────────────
DIAGRAMS['seq_signup'] = SKIN + """
title Sequence Diagram — Sign-up

actor "Learner" as L
participant "SignUpScreen" as S
participant "AuthRepository" as AR
participant "Supabase Auth" as Auth

L -> S : Fill form (name, email, pwd, riwaya)
S -> AR : signUp(email, pwd, metadata)

alt Email available
  AR -> Auth : signUpWithEmail(data)
  Auth --> AR : AuthResponse (new user)
  AR --> S : success
  S --> L : Navigate to CompleteProfile
  L -> S : Set riwaya + daily goal
  S -> AR : updateProfile(metadata)
  AR -> Auth : updateUser()
  Auth --> AR : profile updated
  AR --> S : success
  S --> L : Profile complete
else Email already exists
  Auth --> AR : Error: email taken
  AR --> S : error
  S --> L : Display "Email already registered"
end
"""

# ─── 8. SEQUENCE: RECITATION ────────────────────────────────────────────
DIAGRAMS['sequence_recitation'] = SKIN + """
title Sequence Diagram — Recitation Submission and AI Feedback

actor "Learner" as L
participant "Tahkik App\\n(Flutter)" as App
participant "Tahkik AI Server\\n(Python / FastAPI)" as AI
database "Supabase DB" as DB

L -> App : Open Quran reader
App --> L : Show Surah list

L -> App : Select Surah
App --> L : Show Ayah list

L -> App : Select specific Ayah to recite
App --> L : Show recording screen\\nwith selected Ayah text

L -> App : Press record button
App -> AI : Open WebSocket connection\\n(send reference ayah text)

loop Every ~1 second (streaming)
  App -> AI : Stream audio chunk (PCM 16 kHz)
  AI -> AI : Transcribe with NeMo FastConformer
  AI --> App : Partial transcription text
  App --> L : Display partial text in real-time
end

App -> AI : Close stream (end of recording)

AI -> AI : Run three-model pipeline:\\n① Whisper-Small → transcription + tashkeel errors\\n② NeMo FastConformer → CTC alignment + per-letter timings\\n③ Muaalem → per-letter Tajweed grades

AI --> App : Final feedback response:\\n• corrected transcription\\n• confidence score (0–100 %)\\n• wrong-word list (with positions)\\n• tashkeel errors (missing / wrong harakaat)\\n• per-letter Tajweed violations\\n  (madd, ghunnah, qalqala, tafkheem …)\\n  each with timestamp & severity

App -> DB : Save recitation session\\n(audio URL + feedback JSON)
DB --> App : session_id
App --> L : Display AI feedback:\\n score badge + word highlights\\n + per-letter Tajweed annotations
"""

# ─── 9. SEQUENCE: TEACHER REVIEW ────────────────────────────────────────
DIAGRAMS['seq_teacher'] = SKIN + """
title Sequence Diagram — Teacher Recitation Review

actor "Teacher" as T
participant "Dashboard\\n(React)" as D
participant "Queries" as Q
database "Supabase DB" as DB

T -> D : Open Recitation Review
D -> Q : fetchTeacherRecitations()
Q -> DB : SELECT sessions + profiles
DB --> Q : TeacherRecitation[]
Q --> D : session list
D --> T : Display session queue

T -> D : Select session
D -> Q : fetchSessionTajweed(id)
Q -> DB : SELECT tajweed_results
DB --> Q : TajweedResult[]
Q --> D : Display errors + audio
D --> T : Show review panel

T -> D : Play audio
T -> D : Review AI annotations

alt Override AI annotation
  T -> D : Toggle annotation override
end

T -> D : Add manual feedback + notes
D -> Q : submitTeacherFeedback(data)
Q -> DB : INSERT INTO feedback
DB --> Q : success
Q --> D : feedback saved
D --> T : Show confirmation
"""

# ─── 10. SEQUENCE: PROGRESS ─────────────────────────────────────────────
DIAGRAMS['seq_progress'] = SKIN + """
title Sequence Diagram — Progress Tracking

actor "Learner" as L
participant "ProgressScreen" as PS
database "Supabase DB" as DB

L -> PS : Open Progress tab

PS -> DB : SELECT daily_progress
DB --> PS : DailyProgress[]

PS -> DB : SELECT recitation_sessions
DB --> PS : RecitationSession[]

PS -> DB : SELECT certificates
DB --> PS : Certificate[]

PS --> L : Display charts, streak,\\nrecitation history

opt User taps a session
  L -> PS : Select past session
  PS -> DB : SELECT session detail
  DB --> PS : SessionDetail
  PS --> L : Show audio replay +\\nTajweed feedback
end
"""

# ─── 11. SEQUENCE: ADMIN ────────────────────────────────────────────────
DIAGRAMS['seq_admin'] = SKIN + """
title Sequence Diagram — Admin User Management

actor "Admin" as A
participant "Dashboard\\n(React)" as D
participant "Queries" as Q
database "Supabase DB" as DB

A -> D : Open User Management
D -> Q : fetchUsers()
Q -> DB : SELECT profiles
DB --> Q : Profile[]
Q --> D : user list
D --> A : Display user table

opt Search / filter
  A -> D : Enter search query
  D --> A : Filter results client-side
end

A -> D : Select user / action
D -> Q : updateUserRole(userId, role)
Q -> DB : UPDATE profiles SET role
DB --> Q : updated
Q --> D : success
D --> A : Show updated user list
"""

# ─── 12. CLASS DIAGRAM ──────────────────────────────────────────────────
DIAGRAMS['class_diagram'] = SKIN + """
title Class Diagram — Tahkik Platform

abstract class User {
  -id : UUID
  -email : String
  -name : String
  -role : RoleEnum
  -avatar_url : String
  -created_at : DateTime
  +login() : void
  +logout() : void
}

class Learner {
  -riwaya : String
  -daily_goal : Integer
  +recordRecitation() : void
  +viewProgress() : void
}

class Teacher {
  -qualification : String
  +reviewRecitation() : void
  +issueIjaza() : void
  +manageStudents() : void
}

class Admin {
  +viewAnalytics() : void
  +manageUsers() : void
  +monitorAI() : void
  +manageDailyVerse() : void
}

class Recitation {
  -id : UUID
  -user_id : UUID
  -surah : Integer
  -ayah_start : Integer
  -ayah_end : Integer
  -audio_url : String
  -submitted_at : DateTime
  +submit() : void
}

class Feedback {
  -id : UUID
  -recitation_id : UUID
  -teacher_id : UUID
  -type : FeedbackType
  -confidence_score : Float
  -notes : String
  -created_at : DateTime
  +generate() : void
}

class Subscription {
  -id : UUID
  -user_id : UUID
  -plan_type : PlanEnum
  -start_date : Date
  -end_date : Date
  +isActive() : Boolean
}

class Progress {
  -id : UUID
  -user_id : UUID
  -total_recitations : Integer
  -average_score : Float
  -streak_days : Integer
  +update() : void
}

class Ijaza {
  -id : UUID
  -learner_id : UUID
  -teacher_id : UUID
  -surah : Integer
  -issued_at : DateTime
  +generate() : void
}

class Message {
  -id : UUID
  -sender_id : UUID
  -receiver_id : UUID
  -content : String
  -sent_at : DateTime
  +send() : void
}

class DailyVerse {
  -id : UUID
  -arabic_text : String
  -translation : String
  -surah_name : String
  -ayah_number : Integer
  -is_active : Boolean
  -created_at : DateTime
  +activate() : void
}

class TajweedResult {
  -id : UUID
  -recitation_id : UUID
  -word_index : Integer
  -rule_type : String
  -severity : String
  -start_time : Float
  -end_time : Float
  +flag() : void
}

User <|-- Learner
User <|-- Teacher
User <|-- Admin

Learner "1" -- "0..*" Recitation : submits
Learner "1" -- "1" Subscription : has
Learner "1" -- "1" Progress : tracks
Learner "1" -- "0..*" Ijaza : receives
Teacher "1" -- "0..*" Ijaza : issues
Teacher "1" -- "0..*" Feedback : provides
Recitation "1" -- "0..*" Feedback : receives
Recitation "1" -- "0..*" TajweedResult : has
User "1" -- "0..*" Message : sends
User "1" -- "0..*" Message : receives
Admin "1" -- "0..*" DailyVerse : manages
"""

# ─── 13. SYSTEM ARCHITECTURE ────────────────────────────────────────────
DIAGRAMS['sys_arch'] = SKIN + """
title System Architecture — Tahkik Platform

actor "Learner" as L
actor "Admin" as A
actor "Teacher" as T

package "Client Layer" {
  [Tahkik App\\n(Flutter / Mobile)] as APP
  [Tahkik Dashboard\\n(React / Web)] as DASH
}

package "Backend Layer (Docker Compose)" {
  [Caddy\\n(Reverse Proxy)] as CADDY
  [Go API Server\\n(REST Gateway)] as GO
  [NeMo AI Engine\\n(Python / FastAPI)] as PY
}

cloud "Supabase (BaaS)" {
  database "PostgreSQL DB\\n(RLS Policies)" as PGDB
  [Supabase Storage\\n(Audio Files)] as STORE
  [Supabase Auth\\n(JWT / OAuth)] as AUTH
  [Real-time\\nSubscriptions] as RT
}

L --> APP
A --> DASH
T --> DASH

APP --> AUTH : Authentication
APP --> PGDB : Data queries
APP --> STORE : Audio upload
APP --> PY : WebSocket streaming\\n(real-time audio)

DASH --> AUTH : Authentication
DASH --> PGDB : Data queries
DASH --> RT : Live updates

CADDY --> GO : Proxy REST
CADDY --> PY : Proxy inference
GO --> PY : Audio processing
GO --> PGDB : Read/Write sessions
DASH --> GO : System health\\ntelemetry
"""

# ─── 14. ACTIVITY DIAGRAM: RECITATION ───────────────────────────────────
DIAGRAMS['activity_recitation'] = SKIN + """
title Activity Diagram — Recitation and AI Feedback Flow

start

:Learner opens Quran Reader;

:Browse Mushaf pages;

:Select Surah and Ayah range;

:Tap Record button;

:App opens WebSocket\\nto AI Server;

fork
  :Stream audio chunks\\n(PCM 16kHz);
fork again
  :AI transcribes\\nin real-time;
  :Display partial\\ntranscription;
end fork

:Learner stops recording;

:AI computes final\\nconfidence score;

:AI detects Tajweed errors;

if (Score >= threshold?) then (yes)
  :Display success\\nfeedback (green);
else (no)
  :Highlight errors\\nwith Tajweed rules;
endif

:Save session\\nto Supabase DB;

:Update learner\\nprogress & streak;

stop
"""

# ─── 15. DEPLOYMENT DIAGRAM ─────────────────────────────────────────────
DIAGRAMS['deployment_diagram'] = SKIN + """
title Deployment Diagram — Tahkik Platform

node "Learner Device\\n(iOS / Android)" as MOBILE {
  artifact "Tahkik App\\n(Flutter)" as FAPP
}

node "Browser\\n(Desktop / Tablet)" as BROWSER {
  artifact "Tahkik Dashboard\\n(React SPA)" as RAPP
}

node "DigitalOcean Droplet" as DO {
  node "Docker Compose" as DC {
    artifact "Caddy\\n(Reverse Proxy)" as CADDY
    artifact "Go API Server\\n(REST Gateway)" as GO
    artifact "Python FastAPI\\n(Whisper Inference)" as PY
    artifact "tahkik-small-warsh\\n(Whisper Checkpoint)" as MODEL
  }
}

cloud "Supabase Cloud" as SB {
  database "PostgreSQL" as PG
  artifact "Auth Service" as AUTH
  artifact "Storage" as STR
  artifact "Real-time" as RT
}

FAPP --> CADDY : HTTPS / WSS
RAPP --> CADDY : HTTPS
CADDY --> GO : :8080
CADDY --> PY : :7860
GO --> PY : localhost:7860
GO --> PG : PostgreSQL
FAPP --> AUTH : JWT Auth
FAPP --> PG : Data
FAPP --> STR : Audio files
RAPP --> AUTH : JWT Auth
RAPP --> PG : Data
RAPP --> RT : Subscriptions
PY --> MODEL : loads weights
"""


def generate_all():
    os.makedirs(OUT, exist_ok=True)
    for name, src in DIAGRAMS.items():
        out_path = os.path.join(OUT, f'{name}.png')
        print(f'Generating {name}...', end=' ')
        try:
            # Write temp file, render via web service
            tmp = os.path.join(OUT, f'{name}.puml')
            with open(tmp, 'w') as f:
                f.write(f'@startuml\n{src}\n@enduml\n')
            ok = SERVER.processes_file(tmp, outfile=out_path)
            os.remove(tmp)
            if ok:
                print(f'OK -> {out_path}')
            else:
                print(f'FAILED')
        except Exception as e:
            print(f'ERROR: {e}')

if __name__ == '__main__':
    generate_all()
