import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from save_data import SaveData
from item import Item
from monster import Monster

import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rider's SaveForge - MHS Save Editor")
        self.geometry("600x450")
        
        try:
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
            self.iconbitmap(icon_path)
        except Exception:
            pass
        
        self._apply_theme()
        
        self.items = []
        self.monsters = []
        
        self._create_menu()
        self._create_widgets()
        
    def _apply_theme(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        
        bg_color = "#16213e"
        fg_color = "#e0e0e0"
        accent_color = "#ff6b00" 
        dark_blue = "#0f3460"
        
        self.configure(bg=bg_color)
        
        style.configure(".", background=bg_color, foreground=fg_color, font=('Segoe UI', 10))
        
        style.configure("TNotebook", background=bg_color, borderwidth=0)
        style.configure("TNotebook.Tab", background=dark_blue, foreground=fg_color, padding=[10, 5], font=('Segoe UI', 10, 'bold'), borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", accent_color)], foreground=[("selected", "#ffffff")])
        
        style.configure("TFrame", background=bg_color)
        
        style.configure("TButton", background=dark_blue, foreground=fg_color, borderwidth=0, padding=5, font=('Segoe UI', 10, 'bold'))
        style.map("TButton", background=[("active", accent_color)], foreground=[("active", "#ffffff")])
        
        style.configure("TLabel", background=bg_color, foreground=fg_color)
        
        style.configure("TEntry", fieldbackground=dark_blue, foreground="#ffffff", borderwidth=0, insertcolor="#ffffff")
        
        style.configure("Treeview", background=bg_color, fieldbackground=bg_color, foreground=fg_color, borderwidth=0, rowheight=25)
        style.map("Treeview", background=[("selected", accent_color)], foreground=[("selected", "#ffffff")])
        style.configure("Treeview.Heading", background=dark_blue, foreground=accent_color, font=('Segoe UI', 10, 'bold'), borderwidth=0)
        
        style.configure("TPanedwindow", background=bg_color)

    def _create_menu(self):
        menubar = tk.Menu(self, bg="#0f3460", fg="#e0e0e0", activebackground="#ff6b00", activeforeground="#ffffff", borderwidth=0)
        filemenu = tk.Menu(menubar, tearoff=0, bg="#0f3460", fg="#e0e0e0", activebackground="#ff6b00", activeforeground="#ffffff", borderwidth=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

    def _create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.tab_basic = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_basic, text="Basic")

        self.tab_item = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_item, text="Item")

        self.tab_monster = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_monster, text="Monster")
        
        self._setup_item_tab()
        self._setup_monster_tab()

    def _setup_item_tab(self):
        btn_max = ttk.Button(self.tab_item, text="Maximizar Todos os Itens (999)", command=self.max_all_items)
        btn_max.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Edit frame at bottom
        edit_frame = ttk.Frame(self.tab_item)
        edit_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        ttk.Label(edit_frame, text="Selected Item Count:").pack(side=tk.LEFT, padx=5)
        self.item_count_var = tk.StringVar()
        self.item_count_entry = ttk.Entry(edit_frame, textvariable=self.item_count_var, state=tk.DISABLED)
        self.item_count_entry.pack(side=tk.LEFT, padx=5)
        
        # Treeview for items
        frame_list = ttk.Frame(self.tab_item)
        frame_list.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(frame_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        columns = ("Count", "ID")
        self.item_tree = ttk.Treeview(frame_list, columns=columns, show="headings", yscrollcommand=scrollbar.set)
        self.item_tree.heading("Count", text="Count")
        self.item_tree.heading("ID", text="ID")
        self.item_tree.column("Count", width=100)
        self.item_tree.column("ID", width=100)
        self.item_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.item_tree.yview)
        
        def on_item_count_change(*args):
            if not self.item_tree.selection(): return
            item_id = self.item_tree.selection()[0]
            idx = self.item_tree.index(item_id)
            if idx < len(self.items):
                try:
                    val = int(self.item_count_var.get())
                    self.items[idx].count = val
                    self.item_tree.item(item_id, values=(self.items[idx].count, self.items[idx].id))
                except ValueError:
                    pass

        self.item_count_var.trace_add("write", on_item_count_change)
        
        def on_item_select(event):
            selection = self.item_tree.selection()
            if selection:
                idx = self.item_tree.index(selection[0])
                if idx < len(self.items):
                    self.item_count_entry.config(state=tk.NORMAL)
                    self.item_count_var.set(str(self.items[idx].count))
            else:
                self.item_count_var.set("")
                self.item_count_entry.config(state=tk.DISABLED)

        self.item_tree.bind("<<TreeviewSelect>>", on_item_select)

    def _setup_monster_tab(self):
        paned = ttk.PanedWindow(self.tab_monster, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        frame_left = ttk.Frame(paned, width=150)
        paned.add(frame_left, weight=1)
        
        scrollbar = ttk.Scrollbar(frame_left)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.monster_listbox = tk.Listbox(frame_left, yscrollcommand=scrollbar.set, exportselection=False,
                                          bg="#16213e", fg="#e0e0e0", selectbackground="#ff6b00", selectforeground="#ffffff",
                                          borderwidth=0, highlightthickness=0, font=('Segoe UI', 10))
        self.monster_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.monster_listbox.yview)
        
        self.monster_listbox.bind('<<ListboxSelect>>', self.on_monster_select)
        
        frame_right = ttk.Frame(paned)
        paned.add(frame_right, weight=3)
        
        self.monster_vars = {
            "name": tk.StringVar(),
            "lv": tk.StringVar(),
            "type": tk.StringVar(),
            "hp_plus": tk.StringVar(),
            "attack_plus": tk.StringVar(),
            "defense_plus": tk.StringVar()
        }
        
        labels = [
            ("Name", "name"),
            ("Lv", "lv"),
            ("Type", "type"),
            ("HP+(*3)", "hp_plus"),
            ("Attack+", "attack_plus"),
            ("Defense+(*2)", "defense_plus")
        ]
        
        for i, (text, var_key) in enumerate(labels):
            ttk.Label(frame_right, text=text).grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entry = ttk.Entry(frame_right, textvariable=self.monster_vars[var_key])
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.EW)
            
            self.monster_vars[var_key].trace_add("write", lambda *args, k=var_key: self.on_monster_edit(k))
            
        frame_right.columnconfigure(1, weight=1)
        
        self.current_monster_idx = -1

    def on_monster_select(self, event):
        selection = self.monster_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        if idx < len(self.monsters):
            self.current_monster_idx = idx
            m = self.monsters[idx]
            self.monster_vars["name"].set(m.name)
            self.monster_vars["lv"].set(str(m.lv))
            self.monster_vars["type"].set(str(m.id))
            self.monster_vars["hp_plus"].set(str(m.hp_plus))
            self.monster_vars["attack_plus"].set(str(m.attack_plus))
            self.monster_vars["defense_plus"].set(str(m.defense_plus))

    def on_monster_edit(self, key):
        if self.current_monster_idx < 0 or self.current_monster_idx >= len(self.monsters):
            return
        m = self.monsters[self.current_monster_idx]
        val = self.monster_vars[key].get()
        try:
            if key == "name":
                m.name = val
                self.monster_listbox.delete(self.current_monster_idx)
                self.monster_listbox.insert(self.current_monster_idx, val)
                self.monster_listbox.selection_set(self.current_monster_idx)
            elif key == "lv":
                m.lv = int(val)
            elif key == "type":
                m.id = int(val)
            elif key == "hp_plus":
                m.hp_plus = int(val)
            elif key == "attack_plus":
                m.attack_plus = int(val)
            elif key == "defense_plus":
                m.defense_plus = int(val)
        except ValueError:
            pass 

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            if SaveData.instance().open(filename):
                self.initialize_data()

    def save_file(self):
        if SaveData.instance().save():
            messagebox.showinfo("Success", "File saved successfully!")

    def initialize_data(self):
        self.items.clear()
        for i in self.item_tree.get_children():
            self.item_tree.delete(i)
            
        for index in range(999):
            item = Item(0x60 + index * 8)
            if item.id != 0:
                self.items.append(item)
                self.item_tree.insert("", tk.END, values=(item.count, item.id))
                
        self.monsters.clear()
        self.monster_listbox.delete(0, tk.END)
        self.current_monster_idx = -1
        
        for index in range(400):
            monster = Monster(0x42330 + index * 596)
            if monster.id != 0:
                self.monsters.append(monster)
                self.monster_listbox.insert(tk.END, monster.name)
                
    def max_all_items(self):
        for i, item in enumerate(self.items):
            item.count = 999
            item_id = self.item_tree.get_children()[i]
            self.item_tree.item(item_id, values=(item.count, item.id))

if __name__ == "__main__":
    app = App()
    app.mainloop()
