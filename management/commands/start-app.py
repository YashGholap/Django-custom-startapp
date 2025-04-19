import os
import subprocess
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = "Creates a new Django app with Git, README, and LICENSE"
    
    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help="Name of the app to create")
        # parser.add_argument('--license', type=str, default='MIT', help='License type (default: MIT)')
        
    def handle(self,*args,**options):
        app_name=options['app_name']
        
        try:
            call_command('startapp', app_name)
            self.stdout.write(self.style.SUCCESS(f'App "{app_name}" created'))
            
            app_path = os.path.join(os.getcwd(),app_name)
            
            #Git init
            subprocess.run(['git','init'], cwd=app_path, check=True)
            
            #readme
            readme_path = os.path.join(app_path, 'README.md')
            with open(readme_path, 'w') as f:
                f.write(f"# {app_name}\n\nThis is the `{app_name}` Django app.\n")
                
            #License
            license_path = os.path.join(app_path, 'LICENSE')
            with open(license_path, 'w') as f:
                f.write(f"MIT License\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the \"Software\"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.") 
            
            self.stdout.write(self.style.SUCCESS("Git repo initialized with README and LICENSE"))
            
        except Exception as e:
            raise CommandError(f"Error: {str(e)}")