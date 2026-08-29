# Fei Gao — personal website

This folder is a complete website for GitHub Pages.

## The two design versions

- `index.html` + `style.css` — **dark version** (modeled on hubermanlab.com): deep blue-black, gold accent, serif headlines.
- `warm.html` — **light version** (modeled on yourparentingmojo.com): cream, teal and coral, friendly and approachable. All its styling is inside the file itself.

Whichever file is named `index.html` is the homepage. To switch to the warm
version: rename `index.html` to `dark.html`, then rename `warm.html` to
`index.html` (and the old `style.css` is only used by the dark version).

## How to edit

Open the folder in VS Code and edit the HTML files. Every place that needs
your real content is marked with [square brackets]. Search for `[` to find
them all. To add your photo, put `portrait.jpg` into the `images/` folder
and follow the comment in the HTML near "Replace with your photo".

## How to publish

1. On github.com, create a **public** repository named exactly
   `gaofei9.github.io` (if it exists but is private, make it public in
   Settings → General → Danger Zone → Change visibility).
2. Easiest first publish (no tools needed): open the repository page →
   "Add file" → "Upload files" → drag everything in this folder in → Commit.
3. After 1–2 minutes the site is live at https://gaofei9.github.io

To publish from the terminal instead (after the repository exists):

```
cd ~/gaofei9.github.io
git push -u origin main
```

The first push will ask you to sign in to GitHub.

## Safety notes

- Everything in this repository is public, including old versions of files.
  Never add passwords, keys, or private data.
- Protect the GitHub account itself: strong password + two-factor
  authentication.
