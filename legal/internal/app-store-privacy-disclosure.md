# App Store Connect — Privacy Disclosure and Age Rating

Effective 21 October 2026 · Version 1.0

The answers to enter in App Store Connect under App Privacy and Age Rating. The developer of record is Flaunt Technologies L.L.C-FZ (Meydan Free Zone, Dubai, licence 2654245.01), which must match the Apple Developer Program enrolment exactly, including the "L.L.C-FZ" suffix, and the D-U-N-S record. They follow the Privacy Policy exactly; if the policy changes, change these in the same release.

## App Privacy

**Do you or your third-party partners collect data from this app?** Yes.

**Privacy policy URL:** the public URL of the Privacy Policy. The same URL is linked inside the app from the join sheet and Settings (Guideline 5.1.1).

### Data types collected

Each type is declared with three answers: linked to the user's identity, used for tracking, and purpose.

| Category | Data type | Linked to user | Used for tracking | Purposes |
| --- | --- | --- | --- | --- |
| Contact Info | Email Address | Yes | No | App Functionality (optional recovery email) |
| User Content | Photos or Videos | Yes | No | App Functionality (posts); Other (automated moderation screening) |
| User Content | Other User Content | Yes | No | App Functionality (captions, comments, bio, Form Check frames and results) |
| Identifiers | User ID | Yes | No | App Functionality |
| Identifiers | Device ID | No | No | App Functionality, Analytics (app-generated anonymous identifier, not a hardware or Apple identifier; resets on reinstall) |
| Usage Data | Product Interaction | No | No | Analytics, App Functionality |
| Health & Fitness | Fitness | Yes | No | App Functionality (lift type, weight, Form Check observations) |
| Other Data | Other Data Types | Yes | No | App Functionality (year of birth for the 16+ gate) |

### Data types not collected

Name, phone number, physical address, precise or coarse location, contacts, photo library (add-only access cannot read it), financial info, health records, browsing history, search history (queries are not stored), purchase history, sensitive info beyond year of birth, crash data unless Apple's own crash reporting is enabled (declare Diagnostics > Crash Data if it is).

### Tracking

**Does this app use data for tracking?** No. No data is linked with third-party data for advertising, no advertising identifier is read, and no App Tracking Transparency prompt is shown.

### Third-party partners that receive data

Supabase (database and authentication), Cloudflare (media storage), Google Cloud Vision (moderation frames), Anthropic (Form Check frames), Loudly (track requests), Zoho (support email and recovery codes). None uses the data for its own purposes.

## Age Rating questionnaire

| Question | Answer |
| --- | --- |
| Cartoon or fantasy violence | None |
| Realistic violence | None |
| Prolonged graphic or sadistic realistic violence | None |
| Profanity or crude humour | Infrequent/Mild (user comments, filtered) |
| Mature or suggestive themes | Infrequent/Mild (athletic clothing in user clips) |
| Horror or fear themes | None |
| Medical or treatment information | None (Form Check is labelled as observation, not medical advice) |
| Alcohol, tobacco or drug use or references | None |
| Simulated gambling | None |
| Sexual content or nudity | None (prohibited and screened) |
| Graphic sexual content and nudity | None |
| Unrestricted web access | No |
| Gambling and contests | No |
| User-generated content | Yes |
| Messaging and chat | No |
| Parental controls | Not applicable |
| Age assurance | Self-declared date of birth; under 16 cannot join |

**Resulting rating: 16+.** Set the rating to 16+ regardless of the questionnaire's computed result; the community is designed for 16 and over and the Terms say so.

## User-generated content requirements (Guideline 1.2)

Declare in the review notes that the app meets each requirement, with where to find it:

1. **Filtering objectionable material:** every upload is screened by Google Cloud Vision SafeSearch before publication; text is filtered by a database trigger on write.
2. **Reporting mechanism with timely response:** Report button on every post, comment and profile; 24-hour action commitment in the Terms and Community Guidelines.
3. **Blocking abusive users:** Block and Mute on every profile; block hides both users from each other everywhere.
4. **Published contact information:** Flaunt Technologies L.L.C-FZ, Meydan Grandstand, 6th floor, Meydan Road, Nad Al Sheba, Dubai, United Arab Emirates, biz@flaunt.ae in the app (Settings > Contact us), the Terms, the Privacy Policy, and the App Store listing.

## Other review items

- **Account deletion (5.1.1 v):** self-service in Settings > Delete account; completes within 24 hours.
- **Permission purpose strings:** Camera "To film your lifts"; Microphone "To record gym sound with your clip, only when you turn it on"; Photos (add-only) "To save your clips to your library".
- **Login services (4.8):** not applicable; FLAUNT offers no third-party login.
- **Medical claims (1.4.1):** none made; Form Check is described as observation, not advice, in the app, the Terms and the Privacy Policy.
- **Demo account for review:** not needed; reviewers can browse the community signed out and join with any date of birth showing 16 or over. Provide a short note on where the Report, Block and Delete account controls are.
