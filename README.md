# Fei Gao: personal website

This folder is a complete website for GitHub Pages, with a blog and a
newsletter signup.

## The design

`index.html` is the homepage and `style.css` holds all the styling. The
blush and bronze color scheme comes from the "Blush Bronze" promo image.
The blog pages share the same stylesheet.

## How to edit

**All homepage text lives in `_data/home.yml`.** Open that file and edit
the text to the right of each colon: the headline, the about paragraphs,
the writing themes, the contact wording. It is a plain text file, so
there is no HTML to break, and the file itself explains the few rules at
the top.

**The research page at `/research/` has its own file, `_data/research.yml`**,
holding the research areas and the publication list. The homepage shows
the first three publications from that list automatically.

`index.html` and `research/index.html` hold only the layout, and read
the text from those files. Edit them when you want to move or restyle a
section, not to change wording.

To swap your photo, replace the files in `images/`, keeping the same names.

Nothing goes live until you commit and push. Saving alone does not
publish, because Nextcloud sync and GitHub are separate things.

## The blog

The blog lives at `/blog/`. Write each post as a Markdown file in the
`_posts/` folder. The file name must start with the date, for example
`2026-09-03-my-first-post.md`. At the top of the file, between two `---`
lines, give the post a title, a one-line description, and tags:

```
---
title: "My first post"
description: "What this post is about, in one line."
tags: [motivation]
---
```

The blog has four standing themes, matching the cards on the homepage.
Use these tags so posts group under them:

- `science-of-learning` — memory, attention, neuroscience, research write-ups
- `motivation` — motivation and emotion in learning
- `tools` — mnemonics, spaced practice, retrieval, other techniques
- `books` — notes on books about learning

A post can carry more than one tag, and other tags are fine too. Each tag
gets its own page at `/tag/name/` automatically. The two example posts in
`_posts/` show the format. Replace them or delete them.

You do not need to install anything on the Mac. When you push, GitHub
builds the site with Jekyll and publishes it within a minute or two.

## The newsletter

The signup form on the homepage and the blog pages sends addresses to
Buttondown (account: gaofei9), free for your first 100 subscribers. The
form text is edited in `_data/home.yml` under `newsletter`.

To send a post to subscribers: open buttondown.com, click New email,
paste in the post title and text with a link to the full post, and send.
Buttondown's automatic RSS-to-email is a paid add-on ($9/month), so
sending stays manual until that ever feels worth buying.

Leave double opt-in turned on in Buttondown. Subscribers confirm by email
before they are added, which keeps the list clean and is expected practice.

## How to publish

One-time setup: on github.com, open the repository → Settings → Pages →
"Build and deployment" → set **Source** to **GitHub Actions**. Without this
change, GitHub tries to build the site its old way and the tag pages will
not work.

After that, publish from the terminal:

```
cd ~/Nextcloud/gaofei9.github.io
git add -A
git commit -m "Update site"
git push
```

The first push will ask you to sign in to GitHub. The site is live at
https://gaofei9.github.io a minute or two after each push.

## Safety notes

- Everything in this repository is public, including old versions of files.
  Never add passwords, keys, or private data.
- Protect the GitHub account itself: strong password + two-factor
  authentication.
