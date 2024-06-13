using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace MonsterHunterStories
{
	internal class ViewModel
	{
		public ICommand OpenFileCommand { get; private set; }
		public ICommand SaveFileCommand { get; private set; }


		public ObservableCollection<Item> Items { get; set; } = new ObservableCollection<Item>();
		public ObservableCollection<Monster> Monsters { get; set; } = new ObservableCollection<Monster>();

		public ViewModel()
		{
			OpenFileCommand = new CommandAction(OpenFile);
			SaveFileCommand = new CommandAction(SaveFile);
		}

		private void Initialize()
		{
			Items.Clear();
			for (uint index = 0; index < 60; index++)
			{
				var item = new Item(0x60 + index * 8);
				if (item.ID == 0) continue;

				Items.Add(item);
			}

			Monsters.Clear();
			for (uint index = 0; index < 5; index++)
			{
				var monster = new Monster(0x42330 + index * 596);
				if (monster.ID == 0) continue;

				Monsters.Add(monster);
			}
		}

		private void OpenFile(Object? parameter)
		{
			var dlg = new OpenFileDialog();
			if (dlg.ShowDialog() == false) return;

			SaveData.Instance().Open(dlg.FileName);
			Initialize();
		}

		private void SaveFile(Object? parameter)
		{
			SaveData.Instance().Save();
		}
	}
}
