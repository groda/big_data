# Accessing Project Gutenberg Without Rate Limits: Mirrors, Rsync & CDN Alternatives

Project Gutenberg (often misspelled as "Gutenberg" or similar) is a fantastic repository of curated, mostly public-domain text-based eBooks.

The main site imposes rate limits on downloads and API-like access, which can be very frustrating for bulk or repeated use.

Has anyone set up a full copy of the entire library on a CDN (or similar high-speed, distributed hosting) — ideally one that gets periodically updated (e.g., every few days or weeks) to include new additions?

Many people have addressed this exact issue, since the collection is explicitly designed for wide redistribution (it's all public domain or freely licensed). While there's no single official commercial CDN (like Cloudflare-hosted version), there are excellent established alternatives that effectively bypass rate limits and provide fast, reliable access to near-complete copies. Here's a clear overview of the best current options as of March 2026:

## Official Mirrors and Rsync for Your Own Copy
Project Gutenberg actively encourages mirroring to distribute load and improve access. You can set up your own local copy (or even a public mirror) and update it as often as you want—daily is recommended since new books are added almost every day. This uses rsync, a efficient sync tool that only downloads changes, avoiding full redownloads each time.

- Use **rsync** for efficient incremental updates (only downloads changes, not the whole ~1–2 TB collection each time).
  - Fast/high-speed source examples:
    - `rsync -av --del aleph.gutenberg.org::gutenberg /your/local/path/` (main collection, including texts)
    - `rsync -av --del aleph.gutenberg.org::gutenberg-epub /your/local/path/cache/epub/` (for EPUB/MOBI generated formats)
  - Or from ibiblio: `rsync -av --del rsync.ibiblio.org::gutenberg /your/local/path/`
- Schedule it via cron (Linux/Mac) or Task Scheduler (Windows) to run every night or every few days.
- Public high-speed mirrors (no rate limits like the main site, often university/ISP-hosted with good bandwidth):
  - https://aleph.pglaf.org/ or https://gutenberg.pglaf.org/ (San Diego, USA – fastest for many, includes generated formats; also rsync/ftp)
  - https://www.mirrorservice.org/sites/ftp.ibiblio.org/pub/docs/books/gutenberg/ (UK)
  - Full mirror list: https://www.gutenberg.org/MIRRORS.ALL
- If you want a true "CDN-like" setup, rsync to your own server/storage (e.g., S3 bucket) and front it with CloudFront or similar — many have done exactly this for personal or small-group use.

This is the most up-to-date method (daily possible) and avoids any central rate limits.


## 2. Kiwix ZIM Files (Easiest for Offline/Compressed Full-Library Snapshots)

Kiwix packages the entire library into ZIM files (a compressed, searchable format for offline use). It's not a live CDN, but a single downloadable archive you can host locally or browse with their app. The full English collection is about 83GB (compressed), and they have versions for other languages too.

- **Download**: Grab from https://download.kiwix.org/zim/gutenberg/. Examples (from recent files):
  - Full multilingual: gutenberg_mul_all_2026-01.zim (~100GB, Jan 2026)
  - English: gutenberg_en_all_2026-01.zim (though sizes vary; English is one of the largest at ~80-90GB)
  - Other languages: e.g., gutenberg_fr_all_2026-01.zim (French, ~9.8GB), gutenberg_de_all_2026-01.zim (German, ~10GB)
  
  They represent the complete library at the time of packaging, including texts in various formats.

- **Update frequency**: Kiwix refreshes these every 2-6 months (e.g., dates like 2025-10 to 2026-01 show quarterly-ish updates). You can use tools like kiwix-zim-updater script to automatically check and download newer versions when available.

- **How to use**: Download once, then open with the free Kiwix app (Windows/Linux/Mac/Android/iOS). It has search, bookmarks, and exports. For serving: Use kiwix-serve to host it on your network like a local website.

This is great if you want a portable, updated snapshot without managing syncs yourself.



## Other Notes
- **Torrents**: Old official ones (from ~2010 CD/DVD project) exist but are very outdated (miss thousands of newer books). No recent full-library torrents are widely maintained/official.
- **Custom scripts**: For English texts only, tools like wget on mirrors or Python scrapers work, but rsync/Kiwix are simpler for the whole thing.
- No major commercial CDN exists (likely due to size/cost), but the mirrors + Kiwix cover the need very well.

---

In short, rsync + mirrors give you the most control for a periodically updated copy, while Kiwix is easier for quick offline access. If none fit, you could script a periodic wget/rsync to a personal CDN bucket. Project Gutenberg's [mirroring guide](https://www.gutenberg.org/help/mirroring.html) has more details.
