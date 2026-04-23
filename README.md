![DL Count](https://img.shields.io/github/downloads/turtle-insect/MonsterHunterStories/total.svg)
<p align="center">
  <img src="icon.png" width="200" alt="Rider's SaveForge Icon"/>
</p>

# Rider's SaveForge

A save editing tool for **Monster Hunter Stories** (Nintendo Switch). 
Easily edit your inventory, max out your items, and tweak your monsters' attributes (Name, Level, ID, HP+, Attack+, Defense+).

> **Note on Version Transfer:** This project was originally built in C# (WPF). It has been completely ported to **Python 3** using the native `tkinter` library. This new version requires no external dependencies or compilation steps, maintaining 100% functionality of the original version in a lighter, cross-platform architecture.

# Official Game Site
https://www.monsterhunter.com/stories/ja-jp/  

# Soft
■ Switch  
https://store-jp.nintendo.com/list/software/70010000066339.html  

# Execution Requirements
* Python 3.x installed
* SaveData Backup (extract your saves from the console first)
* SaveData Restore

# How to Run
Open your terminal in the project directory and run:
```bash
python main.py
```

# Steps to Edit
1. **SaveData Backup:** Extract your save data from your console.
2. Open the save editor using `python main.py`.
3. Go to **File > Open** and select your save file (usually named 『mhs_slot_x.sav』 where x = 1, 2, 3...).
4. Perform any editing (Items or Monsters). 
   *(Note: The tool automatically creates a `backup` folder with your original save data when you load a file).*
5. Go to **File > Save** to overwrite your changes to 『mhs_slot_x.sav』.
6. **SaveData Restore:** Inject the modified save back into your console.
