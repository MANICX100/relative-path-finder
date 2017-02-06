import os.path;

print("""__________       .__          __  .__              
\______   \ ____ |  | _____ _/  |_|__|__  __ ____  
 |       _// __ \|  | \__  \\   __\  \  \/ // __ \ 
 |    |   \  ___/|  |__/ __ \|  | |  |\   /\  ___/ 
 |____|_  /\___  >____(____  /__| |__| \_/  \___  >
        \/     \/          \/                   \/ 
__________         __  .__      ___________.__            .___            
\______   \_____ _/  |_|  |__   \_   _____/|__| ____    __| _/___________ 
 |     ___/\__  \\   __\  |  \   |    __)  |  |/    \  / __ |/ __ \_  __ \
 |    |     / __ \|  | |     \  |     \   |  |   |  \/ /_/ \  ___/|  | \/
 |____|    (____  /__| |___|  /  \___  /   |__|___|  /\____ |\___  >__|   
                \/          \/       \/            \/      \/    \/       """);


print("By Danny Kendall\n\n\n");

path1 = raw_input("What is your first path? \n");
path2 = raw_input("What is your second path? \n ");

try:
    result = os.path.relpath(path1, path2);
    print ("Your relative path is: \n " + result)
except ValueError:
    print ("There is no shortcut for this path. Use: \n" + path2);
