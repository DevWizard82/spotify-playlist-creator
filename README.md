# 🎵 Billboard Hot 100 to Spotify Playlist Time Machine

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green.svg)
![Spotify API](https://img.shields.io/badge/API-Spotipy-1DB954.svg)

A Python script that travels back in time to scrape the top 100 songs from the Billboard Hot 100 chart on any given date, and automatically creates a private Spotify playlist for you containing those historical tracks.


## 📖 Overview
Ever wonder what the world was listening to on the day you were born, or on your high school graduation day? This project allows you to input any historical date (`YYYY-MM-DD`), scrapes the Billboard Hot 100 chart for that specific week, and interacts with the Spotify API to build a playable, private playlist directly in your Spotify account.

## ✨ Features
- **Historical Web Scraping:** Extracts the top 100 song titles and artists from the Billboard website.
- **Spotify API Integration:** Uses the Spotipy library to authenticate users and search the Spotify catalog.
- **Automated Playlist Creation:** Generates a new private playlist and populates it with the found tracks.
- **Error Handling:** Gracefully skips tracks that are not available in the Spotify catalog.

## 🛠 Tech Stack
- **Language:** Python
- **Web Scraping:** Requests, BeautifulSoup4 (`bs4`)
- **API Wrapper:** Spotipy
- **Authentication:** OAuth 2.0
