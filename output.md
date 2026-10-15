## Theracube Tester Guide

Modules A to D on the dev deploy · 4 October 2026

## Links

| WHAT                                          | LINK                                         |
|-----------------------------------------------|----------------------------------------------|
| Staff web app (sign in)                       | theracube-dev.vercel.app/sign-in             |
| Patient app (sign in)                         | theracube-dev.vercel.app/app/sign-in         |
| Public booking page                           | theracube-dev.vercel.app/book/mind-health    |
| Public enquiry form                           | theracube-dev.vercel.app/enquire/mind-health |
| Test checklist (record pass, fail and issues) | claude.ai/artifact/QJr9o9wPUPDQa1wdzRjZXo    |

## Logins

Every staff login uses the password Password123$ and belongs to the demo practice Mind Health.

| ROLE             | EMAIL                     | SIGNS IN AT           | USE IT TO TEST                                                         |
|------------------|---------------------------|-----------------------|------------------------------------------------------------------------|
| Owner            | owner@mindhealth.test     | Staff web app         | Settings, team, practice set-up, everything                            |
| Practice manager | manager@mindhealth.test   | Staff web app         | Inquiries, referrals, waitlist, clients, calendar, forms               |
| Clinician        | clinician@mindhealth.test | Staff web app         | Diary, client records, notes, assessments, treatment plans, telehealth |
| Reception        | reception@mindhealth.test | Staff web app         | Front desk, check-in, booking, calendar                                |
| Client           | client@mindhealth.test    | Patient app only      | Signs in by one-time code, see Module B                                |
| Referrer         | referrer@mindhealth.test  | Not the staff web app | Should be refused by the staff web app                                 |

The demo emails do not exist, so nothing sent to them arrives. To test password reset, invitations or the patient app, use your own real email: add yourself in Settings, Team as the owner, or put your email on a client.

## How to test

1. Open the test checklist and fill in the run details: your name, device, browser and screen size.
2. Sign in with the role the story names. Use a private window per role so two logins never share a session.
3. Follow the story, then mark it Pass, Confusing, Fail or Blocked.
4. For anything other than Pass, write what you did, what you expected and what happened in the story's issue box. It saves as you type.
5. Filter by module to test one module at a time. Stories marked out of scope belong to a later release; skip them.

Test on a desktop browser first (Chrome, 1440 wide or larger), then repeat the list screens on a phone.

## Known issues

Already logged. No need to report them again; add a note if you find more detail.

| ISSUE                                                                            | MODULE    |
|----------------------------------------------------------------------------------|-----------|
| Client and referrer logins can get into the staff web app                        | Access    |
| Setting a password under 12 characters keeps the button disabled with no message | Access    |
| Reception cannot see the Cancellations settings                                  | C         |
| Patient app shows appointment times in the phone's timezone, not the practice's  | B         |
| Add member and Invite are separate flows in Settings, Team                       | H (later) |

Out of scope, skip these: invoices, payments and billing (Module E), inbox and messaging (Module F), documents (Module G) and reports. These pages show "Under construction" .

## How each flow is written

Modules A to D follow, one flow at a time. Every flow has the same five parts:

| Who / where    | The login to use and how to reach the screen: a rail item on the left, or a button.   |
|----------------|---------------------------------------------------------------------------------------|
| Steps          | What to press, in order. Words in bold are the exact labels on screen.                |
| You should see | The result, and where the data shows up next.                                         |
| Check also     | Edge cases worth trying: validation, other roles, empty states, cancelling half way.  |
| Checklist      | The story ids in the test checklist that this flow covers. Record your result there.  |

## Things that apply everywhere SH-1 to SH-4

- Create button. The dark button at the top right changes with the screen: New appointment on Calendar, New client on Clients, Walk-in on Reception, Record a referral, Add to waitlist, New form, New note, New plan, Add task on the Dashboard. Inquiries, Assessments, Telehealth and Settings have none. The arrow beside it (More to create) holds Add task.
- Search. Search or jump to in the top bar (or Ctrl+K, or /) finds clients by name, date of birth, phone, email, client number or Medicare, NDIS or DVA number, plus appointments, enquiries, team, services and locations. Enter opens the result.
- Shortcuts. Press ? for the shortcut sheet. Calendar keys: D day, W week, M month, T today, [ and ] to step.
- Side panels. Most "new" and "open" actions open a panel on the right, with the list still visible. The cross or Esc closes it. Leaving with unsaved work asks Leave without saving? with Keep editing or Discard and leave.
- Theme. The sun icon in the top bar switches light and dark.
- AI is not connected on dev. Settings, AI says No AI model is connected. So the scribe, the Assistant, session prep and Draft with AI all show a clear "unavailable" message. That message is the expected result on dev; report it only if you get an error instead.

The demo data is shared with every tester. Use clients with "Test" in the name, or create your own, before you change, cancel or sign anything. Do not cancel or move other people's appointments.

## Module A: getting new clients in

How a person finds the practice and becomes a client: staff sign-in, the public booking page and enquiry form, then Inquiries, Referrals and the Waitlist. The public pages need no login; open them in a private window.

## A1. Staff sign-in AU-1 to AU-6

Who / where: every staff role, one at a time. /sign-in.

1. Enter the Email and Password from page 1 and press Sign in.
2. Note where you land and which widgets show.
3. Open the user menu (your initials, top right) and sign out.

You should see: every role lands on the Dashboard, with that role's widgets. Reception's Dashboard leads with Arrivals; the Reception desk itself is one click away in the rail.

## Check also:

- Wrong password: "Those details did not match an account. " Nothing says whether the email exists. Repeated failures lock the account for a short while, with a Reset your password link.
- Forgot password? sends a reset link. Use your own email (see the note on page 1).
- After signing out, press Back: no client data should show.
- As owner, copy a Settings URL; open it as reception. You should get a named "no access" state, not a blank page.

## A2. Book online PB-1, PB-2, PB-3, PB-4, PM-1

Who / where: a member of the public, private window. /book/mind-health. Keep the staff Calendar open in another window as reception.

Step 4 of 6, Choose a time. The "Your booking" sheet on the right fills in as you choose. All times are Sydney time.

<!-- image -->

1. Answer the cookie banner (Accept or Essential only).
2. Choose a service (step 1 of 6). Tapping a card moves on straight away.
3. Choose a clinician: Any available or a named clinician.
4. Choose where: a location, or By video.
5. Choose a time: pick a day in the calendar, then a time. Days with nothing read "nothing free" when you hover. Picking a time holds it for you.
6. Your details: a bar shows "Your [time] is held. N minutes left" (15 minutes; amber under 2). Fill First name, Last name, Date of birth and a Mobile or Email. Use your own email. Press Continue.
7. Confirm your booking: check the summary, tick I agree to the practice holding and using my details, press Confirm booking.

You should see: You are booked in with What, With, When, Where and a Reference, plus Add to calendar and Change or cancel. On the staff side the appointment appears in the Calendar as Booked with the note "Online booking" . A new person becomes a new client with Came from: online booking; an existing client (same date of birth plus email or mobile) is reused, and a task "Check an online booking for [name]" appears if details differ.

## Check also:

- Press Continue with fields empty: "Please give a first name. " , "Please give a date of birth, day first. " , "Please give a mobile number or an email so the practice can reach you. "
- Confirm booking stays disabled until the agreement is ticked.
- Hold the same time in two browsers and confirm both: the second gets "That time has just gone. Choose another and you will not lose your details. "
- Pick a clinician and location with no times: No times free just now and a Join the waiting list form. Note: this creates an enquiry in Inquiries, not a Waitlist row.
- Change or cancel opens the manage page for that one booking (PM-1).

## A3. Send an enquiry PE-1

<!-- image -->

Who / where: a member of the public. /enquire/mind-health.

<!-- image -->

The public enquiry form.

1. Fill First name, Last name, a Mobile or Email, and How can they help? (required).
2. Optionally pick a service in What are you after? and tick The practice may contact me about this enquiry.
3. Press Send enquiry.

You should see: Thank you, "Your enquiry is with the practice and somebody will be in touch. " As manager, it appears in Inquiries under New enquiry with source Web form. It does not appear in Clients.

Check also: submit with no contact details ("Please give a mobile number or an email so they can reply. ") and with no message ("Please say what you would like help with. "). Something that looks like spam goes to Held for review instead.

## A4. Work an enquiry through to a client EN-1, EN-2

Who / where: manager (reception and clinician can also do this). Rail, Intake, Inquiries.

An enquiry open beside the board. Convert is disabled here because there is no date of birth.

<!-- image -->

1. The Board shows four working stages: New enquiry, Screening, Booked, Intake. The summary strip above counts Open, New, Awaiting follow-up, Urgent and Held for review; press a cell to filter.
2. Press a card. A panel opens on the right with the person's details, In their words, and the actions. Previous enquiry and Next enquiry step through.
3. Under What has happened, type a note and press Add a note or Log a call.
4. On a New enquiry, press Start screening. It moves to Screening.
5. Press Convert to client. If a likely match exists you get This might be somebody you already have: pick the existing record or None of these, create a new client.
6. Or close it: Not proceeding, choose a Reason (for example Went elsewhere, No capacity, Spam), Save.

You should see: the note in the timeline, dated. After converting: Now a client with the new client number, and the person in Clients. A declined enquiry leaves the board; They came back re-opens it as New.

## Check also:

- Convert to client is disabled without a date of birth ("Add a date of birth before converting. "). Web form enquiries have none, and there is no field in the panel to add one, so pick an enquiry that shows a date of birth. If none can be converted, mark EN-1 Blocked and say so.
- The panel has no control to assign an owner, set urgency or set a follow-up date. If the story asks for it, record that.
- Numbers and Attribution show for manager and owner only. Held for review does not show for clinician.
- Email on the panel writes to the person. Only send to your own address.

## A5. Record and work a referral EN-3

Who / where: manager or reception. Rail, Intake, Referrals.

<!-- image -->

Record a referral opens the New referral panel.

1. Press Record a referral (top right). The New referral panel opens.
2. Fill Given name, Family name, Date of birth, Phone.
3. Referrer: pick one on file (Ken Ito, Helen Zhou, Leah Moss), or Record them from the letterhead and type Referrer name, Practice, Provider number, Referrer type.
4. Set Urgency, Expiry date, Sessions authorised and Reason for referral. Press Save referral.
5. Open the new row. Under What happens next: Triage (urgency and a note), then Attach a client (links or creates the client; a possible duplicate offers Link this record), then Mark booked. Or Decline with a reason.

You should see: the row in the list with its expiry and a session bar ("0 of 10 used"). The summary counts Open referrals, Expiring in 30 days, Already lapsed and Sessions at risk. Once a client is attached, Open their record goes to it and the record shows the referral under Funding.

Check also: save with no family name or no referrer ("A family name, as the letter has it. " , "A name or a practice, from the letterhead. "); decline with fewer than 3 characters; the Expiring and Referrers views; filters Stage, Urgency, Expiry. Clinicians cannot add referrers.

## A6. Waitlist: add someone, then offer them a freed slot RE-7, CA-3

Who / where: manager or reception. Rail, Intake, Waitlist; the offer starts in Calendar.

Add to waitlist.

<!-- image -->

1. Press Add to waitlist. In Who is waiting, search for an existing client (someone new must be added in Clients first).
2. Set Who they want to see, Days that suit, Times that suit, Order in the queue (higher is offered first; not clinical urgency) and Notes. Press Add to the waitlist.
3. Open the row. Press Mark triaged. Change Order in the queue or Notes and press Save.
4. To offer a time: in the Calendar, cancel one of your own test appointments, then follow its Open the waitlist link. The A slot is free panel lists Who could take it, most urgent first. Choose how long An offer lasts and press Offer this hour.
5. Back on the entry: They'll take it books it; They can't make it puts them back to waiting.

You should see: the row with Waiting days, Prefers and status New, then Triaged, then Offered, N min left. Accepting books a new appointment, shown in the Calendar. The offer holds nothing: the slot stays free to book until someone accepts.

Check also: add the same client twice ("They are already waiting"); an end time before the start; Take off the waitlist (kept as cancelled, not deleted); the Status and Clinician filters; the empty-slot Waitlist tab in the Calendar's New appointment panel ranks matching people (CA-3).

## A7. Booking page and widget settings MG-10

- Who / where: owner. Settings, Booking and documents, Online booking and Website widgets. 1. Online booking opens Booking page: Take bookings online, the page Address, Notice needed, How far ahead, Hold a time while they type, Clients may cancel themselves up to, what to ask, what the confirmation link allows, and Save. See what a client sees opens the public page. Do not switch Take bookings online off; other testers need the page. 2. Website widgets: Copy the script tag. Under New widget, give a Widget name, pick Which form (Booking or Enquiry) and press Issue it. The new widget lists with the snippet to paste, and Revoke.

You should see: changes survive a reload. Each widget says how often it loaded. Reception sees Online booking but not Website widgets.

## Module B: forms and the patient app

Staff build forms and send them; the client answers from a link or in the patient app. Build as manager (clinician can too; reception can send but not build).

## B1. Build a form, with scoring no story of its own; supports PF-1, AS-1

Who / where: manager. Rail, Documents, Forms, tab Forms.

<!-- image -->

New form: name and kind, then Start building.

1. Press New form (top right). Give a Name and a Kind (Intake, Consent, Clinical, Feedback, Assessment, Check-in). Press Start building. It starts as a draft.
2. Under Form settings fill the Introduction, choose What the person answering sees, and tick Ask for the date of birth to open it if wanted.
3. From Add a question pick a type (Short text, Long text, Choose one, Scale, Yes or no, Signature and so on). On each question set the wording, This has to be answered, and optionally Show this question when for a condition.
4. For an Assessment form, press Scoring, then Add a scale: name it, choose Which questions count, add bands under What the number means, Save this scale. Try a score tests it without saving.
5. Press Preview ("Nothing here is sent or saved"), then Publish.

You should see: the form in the list as v1 live. Opening a live form shows This version is live; press New version to change it. The row's " … " menu has Open, New version, Export the definition and Archive.

Check also: sign in as reception: rows show View, and there is no New form. Scoring on a published form is locked. Instruments lists the PHQ-9, GAD-7, K10 and DASS-21 as available and the commercial ones as Cannot be used. Sent shows completion counts only, never answers.

A live form open in the builder: Form settings, then the questions.

<!-- image -->

## B2. Send a form to a client RE-6, PF-1, PF-2

Who / where: any staff role. Open a test client (Clients, a row, Open record), tab Details, card Intake paperwork. The appointment panel in the Calendar has the same Send a form.

Client record, Details: Funding, The client app and (lower down) Intake paperwork with Send a form.

<!-- image -->

1. Make sure the client's email is your own (More client actions " … " , Edit details, Save changes).
2. Under Send a form, Choose a form (published forms only).
3. Pick How it gets to [name]: Email them the link, Show QR code (for their own phone, now), Hand to client (this device; you are signed out first) or Give them the link (nothing is emailed).
4. Press Send, Show QR code or Make the link to match.
5. Open the link (email, QR on your phone, or copy). The page says Open your form: enter the client's Date of birth, press Open form.
6. Answer. "Your answers save as you go. " Press Send to the practice.

You should see: a confirmation such as "[form] is on its way to [email]. " On the record the intake badge moves Sent, Started, Complete. The client sees "Thank you. Your answers are with the practice. " A scored form's result shows on the record under Outcome trends (Overview and Clinical tabs).

## Check also:

- Send with unanswered required questions: "N questions still need an answer" .
- Wrong date of birth: " ... N tries left before this link locks. " After 8 misses: This link is not valid any more (PF-2).
- QR code: scan with a phone; it opens at the date-of-birth gate (RE-6).
- PF-3 (staff review proposed changes, Mark reviewed): the web app has no screen for this yet. Mark PF-3 Blocked if you cannot find one.

## B3. A risk answer raises a staff-only flag AS-4

<!-- image -->

Who / where: send a PHQ-9 to a test client with your email (B2), answer it as the client, then check as clinician and as reception.

1. Answer item 9 with anything above "Not at all" .
2. As clinician, open the client record.
3. As reception, open the same client and check the Reception desk.

You should see: the client sees a thank-you only, no score. The clinician sees a risk flag on the record and in Needs attention on the Dashboard. Reception sees a warning icon and "Handle with care, notify clinician" , never the flag type or clinical detail.

## B4. Give a client the patient app CL-9, PA-10

Who / where: manager (any staff role can). A test client whose email is your own. Record, tab Details, card The client app.

1. Press Invite to the app. Leave Email empty to use the email on file, or type another. Press Send invitation.
2. Open the invitation email. The page asks for the client's date of birth (Open my app) or for a code it emails you (Send code).
3. You land in the app. Back on the record, the card shows Has access.
4. To end it: Remove access, give a reason. The client is signed out on every device.

You should see: the row move Invited, Has access, Revoked. After Remove access, tapping anything in the app returns to sign-in.

Check also: wrong date of birth on the invitation ("That did not match. Check the date of birth and try again. "); an old link (That invitation has expired); a used link (You already have access, Go to sign in).

## B5. Sign in to the patient app PA-1

Who / where: the client from B4, on a phone. /app/sign-in.

<!-- image -->

Patient app sign-in on a phone.

1. The screen says "We will text or email you a code. There is no password to remember. " Enter the Mobile number or email on the record and press Send me a code.
2. Enter the four digits in Your code and press Sign in. The code lasts ten minutes; three wrong tries need a new code.

You should see: Home. Only clients with active app access (B4) get a code; anyone else sees the same neutral message and no code arrives.

Check also: a wrong code ("That code did not match. Ask for a new one. "); Use a different number. There is no password sign-in, although PA-1 in the checklist mentions one: record PA-1 against the code path only.

## B6. Use the patient app PA-2 to PA-9

Who / where: the signed-in client. The bottom bar: Home, Sessions, Progress, More.

1. Home (PA-2): Your next session with Join for video, or Nothing booked and Book a session. Quick actions Book a session and Forms. If the practice has it on, the daily check-in: How has today been? (0 to 10), an optional note, Share this note with my care team, Save today's check-in (PA-8).
2. Sessions (PA-3, PA-4): Upcoming and Show past sessions. On a session: Add to calendar, Ask to move it (Send the request), Cancel (Cancel this session or Keep it).
3. Book a session (PA-5): Service, Clinician (Anyone available), Where, Time, Check and book, Book this session.
4. More, Forms (PA-6): To complete and Already done. Answer and press Send it; a consent form asks you to type your name and Sign it. No date-of-birth gate here.
5. Progress (PA-7): How things have been, Your goals and the My plan link.
6. More (PA-9): Things that might help, How we contact you, What you have agreed to, Your details (Save), Help and support, Sign out.

## You should see:

- A cancel outside the notice period cancels, and the staff Calendar shows it cancelled. Inside it (24 hours unless the practice changed it) the app refuses with "This practice asks for N hours' notice. Please ring them... " .
- Ask to move it says the session stays booked until the practice replies; the diary does not move.
- A booking from the app appears in the staff Calendar.
- A form sent from the app shows as Complete on the record.
- Your details: name and date of birth are read only; mobile, email and address save.

Check also: Progress with nothing yet (This fills in as you go); My plan shows only goals marked for the app; check-in after saving shows You checked in today and Change it. Known: times show in the phone's timezone (page 2).

## Module C: the core workspace

Dashboard, calendar, clients, the client record, reception and settings. Test as manager first, then repeat the calendar and reception as reception and the client record as clinician.

## C1. Dashboard MG-1, MG-2

Who / where: manager, then clinician and reception. Rail, Dashboard.

Customise: arrows to reorder, S M L for width, cross to remove, Add widget and Done at the top.

<!-- image -->

1. Read the head: the date, Good morning/afternoon/evening, [name] and "N appointments today" .
2. Check Today at a glance, Today's schedule (Start note and Open on the next session), Needs attention (Review opens the client), Practice Pulse (a day opens the calendar), Waitlist, Funded sessions, Tasks and alerts.
3. Manager and owner only: narrow with All locations and All clinicians.
4. Press Customise. On each card use Move left/right, S, M, L for width, or the cross to remove. Add widget opens the widget library. Press Done.
5. Sign out and back in.

You should see: each role's own set of widgets with real numbers. Your layout and filters are kept after signing in again (MG-2). More dashboard controls has Reset the layout, which asks Reset the dashboard? first.

Check also: unticking the last clinician is refused ("At least one has to stay shown"); clinician and reception have no location or clinician filter; money widgets (Payments due, Unbilled) are hidden in this release.

## C2. Find your way round the calendar CA-1, CA-2, CA-9

Who / where: manager or reception. Rail, Calendar.

Find a time.

<!-- image -->

1. Switch views: Day, Work week, Week, Month, Agenda. Use the arrows, the date button and Today.
2. On the left: the month picker, quick jumps (+1 wk to +6 wk), and tick boxes for Clinicians, Locations, Rooms and Appointment types. The panel button beside the views hides it.
3. All clinicians narrows to one person. 15, 30, 60 set the row size.
4. The icons on the right: Privacy mode (hides names), Show cancelled and missed, The full day, and " … " More calendar options (Location, Colour by, Export as ICS).
5. Press the calendar-search icon, Find a time: set Service, Clinician, Length, Location, Within and Time of day.

You should see: appointments with service colours, a red line for now, and "N booked" per day. Two at the same time sit side by side. Find a time lists free times per day with the clinician's first name; check one against the grid (CA-9).

Work week with the filter panel open on the left.

<!-- image -->

## C3. Book an appointment CA-3, CA-4, CA-10, RE-4

Who / where: manager or reception. Calendar: click an empty time, or press New appointment, or Book on a client record.

New appointment, after clicking an empty time.

<!-- image -->

1. The New appointment panel opens with the time you clicked. Choose Existing, New client or Waitlist.
2. Existing: search the caseload in Client by name, phone or funding number. New client: Full name, Date of birth, Mobile, then Add and book.
3. Under Appointment pick Kind, Clinician and Service (fee and length come from the service).
4. Under When and where check Starts and Duration, choose Telehealth or In person, a Location and Room or resource. Repeats makes a series.
5. Check Funding and fee, the Reminders (SMS, Email) and the Appointment note (care team only).
6. Press Book it.

You should see: "Appointment booked" and the block on the grid at once. It also appears on the client record under Appointments and, for today, on Reception.

## Check also:

- Book it stays disabled while a line such as "Choose a client to book. " , "Choose a clinician. " or "Choose a location, or tick By telehealth. " shows.
- New client with the name and date of birth of an existing client: "This may already be on the caseload. " with Book [name] instead (RE-4).
- Kind, Personal time, no client blocks the diary; try booking over it (CA-10).
- Right-click an empty time: Book this time with Existing client, New client, From waitlist.

## C4. Change an appointment: panel, reschedule, cancel, did not attend CA-5, CA-6, CA-11, CA-12

Who / where: manager or reception, on your own test appointment. Calendar, click a block.

The appointment panel beside the grid. Status buttons sit at its foot.

<!-- image -->

1. The appointment panel opens beside the grid: When and where, Appointment details (Status, Reminder, Flag, Resources, Internal note) and More detail. The arrows at the top step to the previous or next appointment; Undo and Redo sit beside them.
2. Change the time, length or room. Each change saves on its own ("Saving" , then "Saved"). Try Undo, then Redo.
3. Set a Flag (Needs follow-up, First visit, Paperwork due, Interpreter booked, Urgent) and add a Resource.
4. Reschedule: the calendar icon on When and where, or right-click, Reschedule it. Pick a time under Move to, press Move to [time], or Leave it where it is. Dragging a block also moves it, with Undo in the message.
5. Cancel (panel foot) or right-click, Cancel the appointment: choose a Reason, Cancelled by (Client, Practice, Clinician), a Note, then Cancel the appointment. Keep the appointment backs out.
6. Did not attend or Record did not attend: Reason, then Record it.

You should see: the panel status buttons follow the visit: Booked offers Confirm, Mark arrived, Did not attend, Cancel; Arrived offers Start session; In session offers Complete. Cancelled and did-not-attend blocks leave the grid unless Show cancelled and missed is on. The Cancellation fee box says Applies or Does not apply, with the hours of notice.

Check also: flag and resource survive a reload; cancel with no reason (refused); cancel as Practice ("No fee when the practice or clinician cancels. "); a series asks Apply the change to. Right-click a block (CA-11): Open, Open in split, Reschedule it, Check the client in, Cancel the appointment, Record did not attend.

<!-- image -->

Cancel appointment, with the fee check.

<!-- image -->

Reschedule: suggested times under Move to.

## C5. Clients list and preview CL-1, CL-2, CL-3, CL-10

Who / where: manager or clinician. Rail, Clients.

A row opened as a preview beside the list.

<!-- image -->

1. Read the columns: Client, Status, Funding (with session pips such as "4 of 10 sessions used"), Primary clinician, Key measure, Next appointment, Risk.
2. Filter with All, Active, New, On hold, Discharged, Funding, Filters, Columns. Search by name, date of birth, Medicare or phone digits.
3. Press a row. A preview opens beside the list; Open record opens the full record, Book books.
4. Manager: Duplicates opens the merge queue. Review a pair, choose which record Survives, carry risk flags across or not, give a reason, Merge into [name].

You should see: the preview with next appointment, contact, funding, latest measure and recent visits, while the list stays usable. After a merge one record remains with both histories.

Check also: clinician sees no Duplicates ("Merging is a manager's decision"); Export downloads; merge only test records.

## C6. Add a client CL-5, RE-4

<!-- image -->

Who / where: manager or reception. Clients, New client. 1. Identity: Full name and Date of birth are required; Preferred name, Pronouns, Gender or sex optional. 2. Contact: Mobile phone, Email, address, Contact by (SMS, Email, Phone). 3. Funding: Add a funder (Medicare, NDIS, DVA and others) with card details. 4. Care team, Status and segmentation (Status, Source, Tags). Press Add client. You should see: "Client added" , the client in the list, and a client number given on save. "); a future date of birth; no ...reminders cannot reach them. , Use this client or Add them

Check also: one name only ("Only one name. Add a surname if you have one. phone and no email (" "); a wrong Medicare number (check digit message); an existing name and date of birth ("This may be someone you already have" anyway).

## C7. The client record CL-4, CL-5, CL-6, CL-8, MG-4, SH-6

Who / where: clinician, then manager and reception. Clients, a row, Open record.

Client record, Overview, with the K10 series and its bands.

<!-- image -->

1. The header has the status, client number, Book, Write note and " … " More client actions (Edit details, Raise a risk flag, Export record). Below it: Funding, Next appointment, Last seen.
2. Tabs: Overview (presenting concern, Outcome trends, treatment plans, recent activity, appointments), Details, Relationships, Appointments, Billing, Documents, Clinical (narrative, safety notes, medications, outcomes, plans), Activity.
3. Edit details: change a phone or address, Save changes, reload.
4. Manager: Details, Who has viewed this record, Show.
5. Raise a risk flag: Kind of concern, Level, Clinical reason, What reception should do, Raise the flag. Clearing one needs a reason.

You should see: the edit kept after reload. Who has viewed lists names, what was read and why (latest 15). Billing says Read-only in this release and offers nothing to change.

## Check also:

- Edit the same client in two windows and save both: "This record changed while you were editing it" with Keep mine and Use theirs (CL-6).
- Reception has no Clinical tab, opens on Details, and sees no scores ("Scores and outcome trends are clinical... ").
- Clear a risk flag with no reason, then with one (MG-4).
- Narrow the window: the tabs become a dropdown (SH-6).
- Documents should be read-only too, but shows Upload, and a file opens Under construction. Report what you find.

## C8. Reception: arrivals and walk-ins RE-1, RE-2, RE-4, RE-5

Who / where: reception. Rail, Reception.

<!-- image -->

Walk-in: the New walk-in panel.

1. The strip counts Arrivals today, In waiting room, Running late, Intake to chase. Filter All, Expected, Arrived, Late, and by location.
2. On one of your own test arrivals press Check in.
3. The clock icon on a row opens: Running late (5, 10, 15, 30 minutes, They did not say), Send a reminder, Override: intake done on paper. Once arrived it also offers Hand to client to fill in (the kiosk; RE-5).
4. Walk-in: Already a client or Not a client yet, then Clinician, Service, Location, Starting, For, and Book and seat them.
5. Phone lookup (right) finds a client by name, phone or Medicare.

You should see: "[name] is checked in" , the row moves to Arrived and the person shows under Waiting room; Admit then takes them in. The calendar block changes status too. A walk-in is booked and seated at once.

Check also: a flagged client (for example Daniel Whitfield) shows a warning icon only, never the flag type (RE2); a walk-in with an existing surname and date of birth offers the existing record (RE-4); clinician sees the desk read-only ("You can view this screen but not check clients in. ").

Reception as reception. The warning icon beside a name marks a risk flag.

<!-- image -->

## C9. Settings, by role MG-5, MG-7, MG-8, AU-6

Who / where: owner, manager, clinician and reception in turn. Rail, Settings.

| ROLE      | SECTIONS SHOWN                                                                                                                                                                                                                                                                                                                  |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Owner     | Your access, Workspace, Activity, Calendar feed, Team and invitations, Practice details, Locations and rooms, Working hours, Services, Cancellations and deposits, The client app, Wellbeing and safety, Change history, Record access, Online booking, Note templates, Website widgets, Security and sign-in, AI, Integrations |
| Manager   | As owner, without Integrations. AI is view only.                                                                                                                                                                                                                                                                                |
| Clinician | Your access, Workspace, Activity, Calendar feed, Working hours, The client app, Wellbeing and safety, Security and sign-in, AI (view only)                                                                                                                                                                                      |
| Reception | Your access, Workspace, Activity, Working hours, The client app, Online booking, Security and sign- in                                                                                                                                                                                                                          |

1. As owner, change one value in Practice details (Save practice details), Locations and rooms (Save location), Services (Save service) and Security and sign-in. Reload each. Put the value back afterwards.
2. Cancellations and deposits: notice hours, late and no-show fees, Save policy. The Reasons list feeds the cancel panel (Rename, Switch off).
3. Team and invitations: Invite someone with your own email (MG-5).
4. Record access: filter by Who, Why, Whose record and dates; Export as CSV (MG-7).

You should see: every change persists after reload. Your access lists the role and permission count, with "Only an owner can change your roles" for others.

Check also: open a settings URL as a role that should not see it (AU-6). Known: reception cannot see Cancellations (page 2).

## C10. When things go wrong ED-1 to ED-4

Who / where: any role, on any editable screen.

- Go offline (DevTools, Network, Offline): one read-only banner for the whole practice.
- Clear the session cookie mid-edit, then sign in again: you return where you were with the draft.
- Open a test record in one window and delete it in another; open a screen as clinician while the owner removes the permission. Each should end in a clear message, not a silent change.

## Module D: clinical work

New in this release: clinical notes and the scribe, assessments, treatment plans and telehealth. Test as clinician unless a step says otherwise. Reception has none of these screens' clinical content.

On dev no AI model is connected and the scribe's consent wording has not been approved. The scribe, the Assistant, Draft with AI and session prep should each say they are unavailable, and the rest of the screen should keep working. Record that as the result for NO-6, NO-7, TP-2, TH-2 and TH-3, and note any error you get instead.

## D1. Write, save and sign a note NO-1, NO-2, NO-4, NO-5

Who / where: clinician. Rail, Clinical, Clinical notes, then New note. Or Write note on a client record, or Start note on the Dashboard's next session.

<!-- image -->

A draft note. Sections marked Required to sign; the Assistant says it is unavailable on dev.

1. In New note pick the Client. Leave Template as Use my default or choose one. Press Start writing.
2. Type into each section. Sections marked Required to sign must be filled. The button by the sign button shows Saving, then Saved (it saves every few seconds).
3. Optional: tick Risk indicated this session in Risk screen and add detail; Add diagram (Genogram, Body chart, Annotated image); Attach a file under Session context.
4. Leave the page, come back to Clinical notes and open the draft again.
5. Press Review and sign. There is no second confirmation: "Signing is final. Later corrections are added as addenda. "

You should see: the draft in the list as Draft with a word count, then Signed. A signed note is Signed and locked with no edit controls. The note shows on the client record and the Dashboard's Notes to sign count drops.

## Check also:

- Sign with a required section empty: "Not ready to sign" naming the empty sections.
- Filters All, Draft, Generated, Signed, Addendum, and Mine or Everyone; search by client or template.
- Ticking Risk indicated prompts a risk flag on the record.
- On dev there are only drafts from 24 Sept. Start your own note on a test client; do not sign another clinician's draft.

## D2. Correct a signed note with an addendum NO-7

Who / where: clinician, on the note you signed in D1.

1. Press Add an addendum. 2. Fill Why is this correction needed? and the Addendum text. Press Add addendum (or Not now).

You should see: the addendum below the signed text, dated and named; the original text unchanged. The note is listed under Addendum. Regenerate for an addendum only appears when a scribe transcript is still held, which cannot happen on dev.

## D3. The scribe and offline drafting NO-6, NO-8, NO-9

Who / where: clinician, in a draft note.

1. Look for the Ambient scribe. When it is ready it shows a consent statement, Language, Tell clinician and client apart, Start capture, Stop and Draft the note from this session.
2. Go offline (DevTools, Network, Offline), keep typing, reload, then go back online.
3. Owner: Settings, Practice details, Edit the clinical narrative in place. Then as clinician edit a narrative field on the record's Clinical tab.

You should see: on dev, "The scribe is not ready" with the reason, and you can still write by hand. Offline: "Offline: saved on this device" , then "Back online: syncing"; a clash offers Keep mine or Use the server version. Inline editing is off until switched on.

## D4. Note templates NO-3

Who / where: manager or owner. Settings, Booking and documents, Note templates.

A live template with its preview.

<!-- image -->

1. The list shows each template with its version (v1 live), type, sections and disciplines. SOAP progress note is the Practice default.
2. Press New template: Name, Type, Create it. Use Add section and set Section name, Helper text, Required to sign. Check Preview. Press Save draft, then Publish version 1.
3. Under Which template a new note opens with, set a default for a discipline.
4. As a clinician of that discipline, start a new note with Use my default.

You should see: the new note opens with that template's sections. A live version says This version is live and cannot be changed; Edit as a new version starts version 2. Clinicians do not see Note templates.

Check also: put the practice default back to what it was, since all testers share it.

## D5. Administer an assessment and read the outcome AS-1, AS-2, AS-3, CL-4

<!-- image -->

Who / where: clinician. Rail, Assessments, card Administer a measure. The same four buttons sit under Outcome trends on the client record.

Assessments: Administer a measure, Enter in session, K10 chosen.

<!-- image -->

1. Pick a Client. Choose how it is taken:
2. Enter in session: choose the Measure (DASS-21, GAD-7, K10, PHQ-9), optionally a Session, answer each item 0 to 4, press Save the result.
3. Record a past result: Date taken, Source, the answers, Record the past result.
4. QR or tablet: choose the form, then hand over or show the QR code.
5. Send to informant: a parent, teacher or carer's name, relationship and your own email, then send.
2. Open the client record, Overview, Outcome trends.

You should see: the score with its band (for K10: moderate from 16, high from 22, very high from 30) and the change since the one before. A past result plots at its own date. Use as baseline sets the comparison point. The hub's Outcomes by measure table and counts update.

Check also: save with items unanswered (kept as part-finished, not scored); compare two measures on one chart (AS-3); reception sees no scores.

## D6. Treatment plans: goals, progress, review TP-1, TP-2, TP-3, PA-7

Who / where: clinician. Rail, Treatment plans, New plan. Or New plan on a client record.

<!-- image -->

New treatment plan.

1. Pick the Client, give a Plan title, press Create plan.
2. On the plan press Add goal, write the Goal, press Add. Add at least one before activating.
3. Press Activate plan.
4. On a goal record progress: Progress %, Note, Record.
5. When due, press Mark reviewed.
6. Reports: New report, choose For the client, For the referrer or GP, or For the funder; Generate PDF, Sign now, Send secure link to your own email (TP-3).

You should see: the plan in the list (Active, Review due, Stalled, All) with progress and goal count, and on the client record under Treatment plans. Goals read On track, At risk, Achieved or Not met. Goals marked for the app show in the patient app's My plan (PA-7).

Check also: activate with no goals ("Add at least one goal before activating. "); Draft with AI says AI drafting is unavailable on dev, with Create by hand instead (TP-2). Dev has no plans yet, so the list starts with No plans here yet.

## D7. Telehealth TH-1, TH-2, TH-3

Who / where: clinician. Rail, Telehealth, or a telehealth appointment in the Calendar.

Telehealth: this week's sessions.

<!-- image -->

1. The page lists This week's video sessions with When, Client, Clinician and State (Link ready, Ready to join, In progress, Finished).
2. On your own test telehealth appointment press Join (or in the appointment panel, Join, then Join as host).
3. In the appointment panel, Copy link gives the client's join link. Open it in a private window. In the patient app the client sees Join the video call.
4. Prep asks for a session summary; Scribe opens the note's scribe.

You should see: the video room opens in a new tab as host, and the panel says the call is not recorded. The state moves to In progress. Prep and Scribe say they are unavailable on dev, and nothing new is stored on the record.

Check also: Join is disabled on a cancelled session; reception sees the status but cannot host. Book a test telehealth appointment for yourself (C3, tick Telehealth) rather than joining a seeded one.

## D8. Module D settings MG-6, MG-7, CL-8

Who / where: owner. Settings: AI, Note templates (D4), Record access.

1. AI: switches for Ambient scribe, Remove identifiers before text is sent to a model and others; Transcript retention, Keep the text transcript for (Never, 1, 7, 30, 60, 90 days, Always; default 7); Consent wording and Approve this wording; Monthly AI budget; Providers; Where your data lives (Australia).
2. Record access: every read of health information, with Who, Whose record, What and Why. Filter and Export as CSV.

You should see: AI switches save at once and are recorded. Manager and clinician see AI read only ("Only the practice owner can change these. "). Record access shows names, not raw ids.

Check also: leave retention and consent wording as you found them; they are practice-wide.

## Phone and tablet SH-5, CA-13

Clients, Inquiries, Referrals, Waitlist and Assessments share one phone layout. Open each on a phone, or narrow a desktop browser below about 880 wide. The rail becomes a bottom bar (Dashboard, Calendar, Clients, Reception, More). Each list screen should show, top to bottom:

1. The title, with at most two small buttons beside it.
2. A folded summary box. Tap it to open the counts.
3. One row: a full-width search and a square " … " button (Views, filters and actions) holding views and filters, with a dot when a filter is on.
4. Compact two-line rows: name in bold, key details below, a status chip and a " … " for row actions (for example Open enquiry).
5. A pager at the bottom when there is more than one page.

Report it if a screen scrolls sideways, cuts off text in the search box or summary, or looks different from the others. Inquiries on a phone is a list grouped by stage; Board, Numbers, Attribution and Held for review are in the " … " menu, with the stage filter below them. In the Calendar on a phone, Week is a column grid and an appointment opens full screen (CA-13).

<!-- image -->