# Fei Gao: personal website

This folder is a complete website for GitHub Pages, with a blog and a
newsletter signup.

## The two design versions

Both versions now share the same blush and bronze color scheme, taken from
the "Blush Bronze" promo image in this folder.

- `index.html` + `style.css`: the editorial version. Serif headlines, a
  sharper grid, bronze headings on blush pink.
- `warm.html`: the friendly version. Rounded buttons, a wave divider, the
  same colors. All its styling is inside the file itself.

Whichever file is named `index.html` is the homepage. To switch to the warm
version, rename `index.html` to `editorial.html`, then rename `warm.html`
to `index.html`. The blog pages use `style.css` in either case.

## How to edit

Open the folder in VS Code and edit the HTML files. Every place that needs
your real content is marked with [square brackets]. Search for `[` to find
them all. To add your photo, put `portrait.jpg` into the `images/` folder
and follow the comment in the HTML near "Replace with your photo".

## The blog

The blog lives at `/blog/`. Write each post as a Markdown file in the
`_posts/` folder. The file name must start with the date, for example
`2026-09-03-my-first-post.md`. At the top of the file, between two `---`
lines, give the post a title, a one-line description, and tags:

```
---
title: "My first post"
description: "What this post is about, in one line."
tags: [research, notes]
---
```

Each tag gets its own page at `/tag/name/` automatically. The two example
posts in `_posts/` show the format. Replace them or delete them.

You do not need to install anything on the Mac. When you push, GitHub
builds the site with Jekyll and publishes it within a minute or two.

## The newsletter

The signup form on the blog pages sends addresses to Buttondown, a
newsletter service that is free for your first 100 subscribers.

1. Create an account at buttondown.com.
2. In `_includes/newsletter.html`, replace `YOUR_BUTTONDOWN_USERNAME` with
   your Buttondown username. It appears once.
3. In Buttondown, open Settings → RSS and add the feed
   `https://gaofei9.github.io/feed.xml`. After that, every new post goes to
   your subscribers by email without any extra step from you.

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
