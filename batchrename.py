import asana

print("Hello! This is a quick script to mass rename tasks in asana, please follow the inputs below!\nNote: To paste into this console it is easiest to right click and selete 'Paste' as crtl+v does not work\n")

print("To get your access token go to https://developers.asana.com/docs/authentication-quick-start\n")

#gets user to enter access token to make sure they have access
MY_PERSONAL_ACCESS_TOKEN = input("PERSONAL ACCESS TOKEN: ")

client = asana.Client.access_token(MY_PERSONAL_ACCESS_TOKEN)
client.LOG_ASANA_CHANGE_WARNINGS = False

#prints users name to confirm access/they are logged in correctly
print("Access Token Accepted - Logged in as: " + client.users.me()['name'])

#user input to select project to update
print("\nTo find the Project ID - please copy the numbers here in any project - \nhttps://app.asana.com/0/################/list\n")

#function to update tasks based on old text (find) and new text (replace).  Also provides user the total number of tasks updated
def update_tasks():
  projectid = input("Project ID: ")
  project_name = client.projects.get_project(projectid)["name"]

  print("Project Accepted - Project Name: " + project_name)

  tasks = client.projects.tasks(projectid)

  print("\nPlease enter the old text (text to be replaced) with the new text (text that it will replace it with) below\n")

  old_text = input("Old Text: ")
  new_text = input("New Text: ")

  count = 0

  for task in tasks:
    if old_text in task['name']:
      client.tasks.update(task['gid'], {'name': task['name'].replace(old_text, new_text)})
      count += 1

  print(count,"Tasks Updated Successfully\n")

  print("to update more tasks, continue below.\n")

while True:
  update_tasks()
