# Fei Gao: personal website

This folder is a complete website for GitHub Pages, with a blog and a
newsletter signup.

## The design

`index.html` is the homepage and `style.css` holds all the styling. The
blush and bronze color scheme comes from the "Blush Bronze" promo image.
The blog pages share the same stylesheet.

## How to edit

Open the folder in VS Code and edit `index.html`. To swap your photo,
replace the files in `images/`, keeping the same names.

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
