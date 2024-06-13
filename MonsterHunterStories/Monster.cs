using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MonsterHunterStories
{
	internal class Monster
	{
		private readonly uint mAddress;

		public Monster(uint address)
		{
			mAddress = address;
		}

		public String Name
		{
			get => SaveData.Instance().ReadText(mAddress, 30);
			set => SaveData.Instance().WriteText(mAddress, 30, value);
		}

		public uint ID
		{
			get => SaveData.Instance().ReadNumber(mAddress + 60, 2);
			set => SaveData.Instance().WriteNumber(mAddress + 60, 2, value);
		}

		public uint Lv
		{
			get => SaveData.Instance().ReadNumber(mAddress + 104, 1);
			set => Util.WriteNumber(mAddress + 104, 1, 1, 99, value);
		}
	}
}
