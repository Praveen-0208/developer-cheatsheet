# Project Name

A Personal Tech Cheatsheet. A more organized and developer specific notes app, where we can save common bug fix methods, best practises we find on the internet or some git command we always forget in one centralised place, in the form of plain text or screenshots. We group each entry and tag them with a relevant term that can be used to search and retrieve that particular entry from the server.

> This project was built as a part ot [PythonToProject Bootcamp by TheLearningDev](https://bhavaniravi.gumroad.com/l/LaFSj)

## Feature list

1. The user logs in / signs up(Github or Email)
2. Inputs an entry
   - User can input anything(say like a screenshot or some random terminal command).
   - User has to add that entry to an existing group or create a new group.
   - Add a tag or relevant term to that input for easier searching.
3. Submits the entry.
4. Show his recent entries on a screen.
5. User can edit an existing entry.
6. User can also search for his older entries using the search bar.
7. A small recommendation while searching and adding new entries.
8. A Trash bin feature to store the deleted entries.
9. Automatic trash bin clean in 30 days.

## Architecture/Flow Diagram

![developer-cheatsheet (2)](https://user-images.githubusercontent.com/62542574/127533189-3c015557-898a-4b50-b11e-d09e852d1372.png)

## API Design

List all the APIs it's methods, request and response params

> Add the API table here

| Action                                                                                     |      Table Name       | REST Method |   Endpoint    | Reponse | Error                          |
| ------------------------------------------------------------------------------------------ | :-------------------: | :---------: | :-----------: | :-----: | ------------------------------ |
| Submit entry                                                                               |        entries        |    POST     |   /entries    |   201   | incorrect params, server error |
| Get recent Entries(also should be able to get data based on tags and groups through query) |        entries        |     GET     |   /entries    |   200   | no data present, server error  |
| Edit an entry                                                                              |        entries        |     PUT     | /entries/{id} |   201   | incorrect params, server error |
| Get single entry                                                                           |        entries        |     GET     | /entries/{id} |   200   | invalid id, server error       |
| Delete(soft) an entry                                                                      |        entries        |   DELETE    | /entries/{id} |   200   | server error                   |
| Create a group                                                                             |        groups         |    POST     |    /groups    |   201   | incorrect params, server error |
| Get all groups                                                                             |        groups         |     GET     |    /groups    |   200   | no data present, server error  |
| Edit a group                                                                               |        groups         |     PUT     | /groups/{id}  |   201   | incorrect params, server error |
| Delete(soft) a group                                                                       |        groups         |   DELETE    | /groups/{id}  |   201   | server error                   |
| Create a tag                                                                               |         tags          |    POST     |     /tags     |   201   | incorrect params, server error |
| Get all tags                                                                               |         tags          |     GET     |     /tags     |   200   | no data present, server error  |
| Edit a tag                                                                                 |         tags          |     PUT     |  /tags/{id}   |   201   | incorrect params, server error |
| Delete(soft) a tag                                                                         |         tags          |   DELETE    |  /tags/{id}   |   201   | server error                   |
| Hard delete data after 30 days                                                             | entries, groups, tags |   DELETE    |    /trash     |   200   | server error                   |
| Create a user                                                                              |         user          |    POST     |     /user     |   200   | incorrect params, server error |
| Get user info                                                                              |         user          |     GET     |  /user/{id}   |   200   | incorrect id, server error     |

## DB Design Diagram

> Add the DB design table here

![db-design](https://user-images.githubusercontent.com/62542574/127536082-a219173f-4b13-4f74-8461-ba9a88c76391.png)

## Coding Issues and Learning

## Deployment Instructions

## Repo Setup

> Add How to setup and run your app
> This is what you will use to deploy your app, so create a seperate requirements.txt file here
