using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Word = Microsoft.Office.Interop.Word;
using System.Reflection;
using Microsoft.Office.Interop.Word;
using System.Runtime.InteropServices;
using Excel = Microsoft.Office.Interop.Excel;

namespace Find_and_Create
{
    class Program
    {
        static void Main(string[] args)
        {

            object FileName = @"Шукшина120.doc";
            object rOnly = true;
            object SaveChanges = false;
            object MissingObj = System.Reflection.Missing.Value;

            Word.Application app = new Word.Application();
            Word.Document doc = null;
            Word.Range range = null;
            

        }
       
    }
}