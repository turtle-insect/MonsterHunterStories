using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MonsterHunterStories
{
	internal class Item
	{
		private readonly uint mAddress;

		public Item(uint address)
		{
			mAddress = address;
		}

		public uint ID
		{
			get => SaveData.Instance().ReadNumber(mAddress, 2);
		}

		public uint Count
		{
			get => SaveData.Instance().ReadNumber(mAddress + 2, 2);
			set => Util.WriteNumber(mAddress, 2, 0, 99, value);
		}
	}
}
