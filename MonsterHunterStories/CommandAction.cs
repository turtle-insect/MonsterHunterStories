using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace MonsterHunterStories
{
	internal class CommandAction : ICommand
	{
#pragma warning disable CS0067
		// no use
		public event EventHandler? CanExecuteChanged;
#pragma warning restore CS0067

		private readonly Action<Object?> mAction;

		public CommandAction(Action<Object?> action) => mAction = action;

		public bool CanExecute(Object? parameter) => true;

		public void Execute(Object? parameter) => mAction(parameter);
	}
}
