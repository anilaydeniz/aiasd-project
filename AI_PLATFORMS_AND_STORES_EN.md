# Platforms and Stores: What You Can Build and Where You Can Publish

AI-Assisted Software Development · Atlas University · Fall 2026–2027

*Prof. Dr. Vedat Coşkun · Türkçesi: [`AI_PLATFORMS_AND_STORES_TR.md`](AI_PLATFORMS_AND_STORES_TR.md)*

Your project ships as a **mobile app, a web client and a server**, and the mobile app
must be **installed from a public store** by the end of the term. This handout answers
the question that every one of you asks in Week 2: *with the laptop and the phone that I
have, what can I build, and which store can I actually reach?* Read it before you write
§6 (technical stack) and §12 (risks) of your proposal.

Fees, lead times and store policies change. The numbers in this handout are the ones that
applied when it was written; check the store's own page before you commit to a plan.

# 1. The rules

- **You publish to at least one public store**, and which one is your choice: Google
  Play, Huawei AppGallery, Samsung Galaxy Store or the Apple App Store. One store is
  enough. Every combination of laptop and phone in this class can reach at least one of
  them (§3).
- **Native Android, native iOS or hybrid: all three are accepted.** Native iOS means that
  you need a Mac and Apple's yearly membership; native Android means that you serve one
  platform only; hybrid (one code base written in a cross-platform framework) gives you
  both platforms from one code base. Choose what you can ship and justify it in §6.
- **The defence is run from the store-installed build**, on a phone of that platform,
  which is either yours or one that you borrow in the room. If you publish to one store
  and your own phone is the other platform, bring the app on your own phone too, so that
  the examiner sees it on both.
- **A store publication is the only thing that counts as "shipped".** A developer build
  on your own phone is how you test and demonstrate; it is not how you publish.

# 2. Native or hybrid?

| | Native | Hybrid |
|---|---|---|
| Android | Kotlin + Jetpack Compose (Android Studio) | Flutter (Dart), React Native / Expo (TypeScript), Capacitor (web tech) |
| iOS | Swift + SwiftUI (Xcode, **Mac only**) | the same code base as above; the iOS build needs a Mac or a hosted build service (a company that builds the app on its own Macs for you) |
| Code bases | two, if you want both platforms | one |
| Web client | you write it separately | Flutter and Expo build for the web too; Capacitor *is* the web client |
| Cost of the iOS side | a Mac + the Apple Developer membership | the same; hybrid does not remove Apple's fee |
| Best when | you already know the language, or you target one platform only | you want both platforms from one code base, or you have a Windows laptop and want iOS too |

The chatbot inside your app (Weeks 6–7) talks to *your server*, so it does not care which
mobile framework you chose. The checker does not care either. Choose what you can ship.

# 3. Your laptop + your phone → your paths

Every row is a setup that someone in this class has. An **X** means that this path leads
to that store; a blank cell means that it does not, whatever you do.

| Laptop + phone | You build | Google Play | AppGallery | Galaxy Store | App Store |
|---|---|:---:|:---:|:---:|:---:|
| **Mac + Android** | native Android (Kotlin) | X | X | X | |
| | native iOS (Swift) \*\* | | | | X |
| | hybrid | X | X | X | X |
| **Mac + iPhone** | native Android (Kotlin) \*\* | X | X | X | |
| | native iOS (Swift) | | | | X |
| | hybrid | X | X | X | X |
| **Windows + Android** | native Android (Kotlin) | X | X | X | |
| | native iOS (Swift) | | | | |
| | hybrid | X | X | X | X\* |
| **Windows + iPhone** | native Android (Kotlin) \*\* | X | X | X | |
| | native iOS (Swift) | | | | |
| | hybrid | X | X | X | X\* |

\*\* Your phone is the other platform, so you develop and test on the emulator or the
simulator (a program on your laptop that behaves like a phone).

\* From Windows the iOS binary (the compiled app file) is built in the cloud by a service
such as Expo EAS or Codemagic, and the Apple membership is still needed. Native iOS from
Windows does not exist, because Xcode runs only on a Mac. Every App Store cell also
assumes the ≈ 99 $/year membership (§4).

Read the same table by column: **three of the four stores are open to everyone**, with any
laptop, any phone and any of the three ways of building. The App Store is the one store
that depends on what you own.

Two facts are hidden in the table:

- **You do not need your own Android phone to publish to an Android store.** The
  emulator in Android Studio is enough to develop and test, and the store accepts the
  package either way. One exception: Google Play asks a new personal account to confirm
  once, in the Play Console app, on a real Android phone (Android 10 or later; an emulator
  is not accepted). A classmate's phone, borrowed for one minute, is enough.
- **You do need a Mac to build native iOS.** Windows users who want the App Store go
  through Expo EAS or Codemagic, which build the iOS binary in the cloud, but the Apple
  membership is still yours to pay.

# 4. The stores

| | Google Play | Huawei AppGallery | Samsung Galaxy Store | Apple App Store |
|---|---|---|---|---|
| Developer fee | one-time (≈ 25 $) | free | free | yearly (≈ 99 $) |
| Registration | a Google account, an identity check and, once, a real Android phone | a Huawei ID, an identity document and a few days' approval | a Samsung account and seller approval | an Apple ID, an identity check and payment |
| Build from | Mac or Windows | Mac or Windows | Mac or Windows | Mac (or a hosted build) |
| Before release | new personal accounts must run a closed test (a test open only to named testers) with 12 testers for 14 days | review, which takes a few days | review, which takes a few days | review, which typically takes days and can end in a rejection |
| Reach in this class | almost every Android phone | Huawei phones; other Android users can install the AppGallery app | Samsung phones; other Android users can install Galaxy Store | every iPhone |
| Watch out for | the closed-test rule above: plan the 12 testers and 14 days into Week 9 instead of discovering the rule in Week 10 | apps that depend on Google services (Firebase, Google Maps, Google Sign-In) do not run on Huawei phones and may be refused | — | the only paid route, and the only one that needs a Mac |
| What you pay in total | ≈ 25 $, once | nothing | nothing | ≈ 99 $ every year, with no student discount |

Two consequences follow:

- **Google Play's test-track rule is a gift if you plan for it.** Twelve testers for
  fourteen days is exactly the beta week (Week 9) with your classmates as testers, and
  those testers are your `contributors_09.json`. It is a disaster if you first hear of
  the rule in Week 10. The rule applies to new *personal* accounts only.
- **Do not depend on Google services.** Your login is by e-mail code or OTP from *your*
  server; keep it that way, and your app runs on every store. If you need maps or push
  notifications, pick a provider that is not tied to one store.
