# Setup Card — the whole thing on one page

**AI-Assisted Software Development · Atlas University · Fall 2026–2027**

Keep this page open. Everything that you need to run during the whole term is on this
page.

---

## Once, before Week 1

**1 · Create your repository.** On the course template (a ready-made repository that
GitHub copies for you), click **Use this template → Create a new repository**. Name it
`aiasd-project`. Set it to **Private**, because the form opens with Public selected.
Then go to **Settings → Collaborators → Add people** and add `VedatCOSKUN`.

**2 · Let your computer talk to GitHub.** Passwords stopped working for this purpose in
2021. Do this step once, and you never need to do it again:

```bash
brew install gh          # Windows: winget install GitHub.cli
gh auth login
```

Answer the questions in this order: `GitHub.com` → `HTTPS` → `Y` → `Login with a web browser`.

*Can you not install software on your machine?* Then use a token instead (a token is a
long random string that stands in for your password). Go to **Settings → Developer
settings → Personal access tokens → Tokens (classic) → Generate new token (classic)**,
tick exactly one box, which is **`repo`**, and copy the token. When git asks for a
password, paste the token. Treat it like the password to your whole account: never put
it in a file, in a chat, or in a commit.

**3 · Copy it to your machine.**

```bash
git clone https://github.com/<your-username>/aiasd-project.git
cd aiasd-project
```

**4 · Say who you are, and push.** Open `student.json` and fill in all five fields. The
`section` field is `en` or `tr`. Then run:

```bash
git add student.json
git commit -m "week01: student identity"
git push
```

**If that push works, you are done.** That push is the whole test.

---

## Every week, the same four

```bash
python .github/check_deliverables.py

git add .
git commit -m "week01: what I did"
git push
```

Nothing else changes for twelve weeks. Only the commit message changes. Run the checker
(the first command, which looks for the files that the week requires) as often as you
like. It is a to-do list, not a grade, and running it costs nothing.

When a week needs them, you run two more commands:

```bash
pip install -r weekNN/requirements.txt
streamlit run app.py
```

---

## Course files arrive by themselves

Every time you run `python .github/check_deliverables.py`, it also brings the course's
files into your repository. It brings a new week's folder when that week is published,
and it brings any course document (`AI_*`) that changed at the root. It never touches a
file that you already have in a week folder. What arrives is untracked (git sees the
files but does not record them yet) until you run `git add .`, and the checker lists
these files. The section below describes the manual way, for when you are offline.

## Two remotes, two very different commands

Your repository has a remote called `origin` (a remote is an address of a copy of your
repository on another computer), and `origin` is your own copy on GitHub. Some weeks
also hand you a starter folder from the course template, and for that you add a second
remote called `template`. These two remotes are not interchangeable.

| | |
|---|---|
| `git pull` | This command pulls from `origin`, which is your own repository, for example after you worked on another machine or edited a file in the browser. It is normal, everyday and safe. |
| `git pull template main` | **Never run this command.** |

The template is a separate repository that has no history in common with yours,
because your copy was created from it and not cloned from it. Merging the two (to merge
means to ask git to combine the two histories) makes git try to reconcile every file at
once: your filled-in `student.json` against the blank one, your finished `hello.py`
against the stub, and your work against the scaffold. You would spend the lecture
untangling conflicts, and a `git pull` that once succeeded keeps trying to do the same
thing again every time.

Instead, take only the one path that you actually want:

```bash
git remote add template https://github.com/vedatcoskun-course/aiasd-template.git   # once, ever
git fetch template
git checkout template/main -- week06
```

These commands copy exactly the path that you name, and they touch nothing else. Run
them **before** you write anything in that folder. If you run them afterwards, they
overwrite your work.

---

## When something goes wrong

> **Read the LAST line of an error, not the first.** Git prints the diagnosis at the
> bottom. The lines above it are context.

| What you see | What it means |
|---|---|
| `Authentication failed`<br>`could not read Username for 'https://github.com'` | GitHub does not know who you are. Run `gh auth login`. If it still fails, run `gh auth status`, because you may be signed in as the wrong account. |
| `Support for password authentication was removed` | This has the same cause. Your GitHub password is not usable here, and retyping it will not help. |
| `! [rejected] main -> main (fetch first)` | GitHub has a commit that you do not have, usually because you edited a file in the browser. Run `git pull --rebase`, then push again. |
| `nothing to commit, working tree clean` | Git sees no change. Either the editor did not save, or you are in the wrong folder. Run `pwd` and look at the folder it prints. |
| `fatal: not a git repository` | You are outside the project. Run `cd` into `aiasd-project` and try again. |
| `index.lock ... File exists` | A git command was interrupted. Run `rm -f .git/index.lock` and retry. |
| Checker says *Cannot tell which week it is* | This is the first run, and there is no network. Connect once and run it again; after that, it works offline. |
| `command not found: python` | Try `python3` instead. On macOS, `python3` is usually the one that exists. |
| `refusing to merge unrelated histories` | You pulled from `template` instead of `origin`. Do not pass `--allow-unrelated-histories`; see the section above. |

---

**Still stuck?** Ask an AI assistant, but be sceptical on git authentication
specifically. Authentication changed in 2021, and most of the internet still describes
the old way. If you are told to use your GitHub password, or to run `git config
credential.helper store`, that advice is out of date. Ignore it and come back to this
card.

The full weekly routine is in
[`AI_WEEKLY_WORKFLOW_STUDENT_EN.md`](AI_WEEKLY_WORKFLOW_STUDENT_EN.md). It says what the
marks are for, what happens at the end of each lecture, and what to do if you cannot be
there.
