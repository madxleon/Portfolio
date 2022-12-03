using System.Windows.Forms;
using Autodesk.AutoCAD.Runtime;



[assembly: CommandClass(typeof(AutoCAD_Plugin.Class))]

namespace AutoCAD_Plugin
{
    public class Class : IExtensionApplication
    {

        public void ShowMessage(string msg)
        {
            MessageBox.Show(msg);
        }


        public void Initialize()
        {
            MessageBox.Show("Плагин запущен!", "AutoCAD_Plugin");
        }
   


        public void Terminate()
        {            
            string message = "Плагин закрывается";
            MessageBox.Show(message, "AutoCAD_Plugin", MessageBoxButtons.OK); 
        }

        
        [CommandMethod("Testing")]
        public void MyCommand()
        {
            MessageBox.Show("Супер, работает!", "AutoCAD_Plugin");           
        }
    }
}
 