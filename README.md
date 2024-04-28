# <img src="https://i.ibb.co/v4jzr3D/1710963331318.png" width="100"/>

# About
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
 
- A social network with an API built in Java (Spring Boot) and the back/frontend in Python (Flask), JavaScript (HTMX) and HTML/CSS.
- The API repository is <a href="https://github.com/docafavarato/linkupapi">here</a>
- Author: <a href="https://www.linkedin.com/in/favarato/">João Pedro Favarato</a>

# Features
# User related
- ## User session
  - Session control for different users with Flask's `session` module. Upon login, each user is assigned a unique session identifier.

- ## User login/register
  - When registering, the user information in inserted into the API. When trying to log in, the system verifies the credentials based on the provided email.

    ![image](https://github.com/docafavarato/linkUp/assets/98183878/b28a8582-21ca-46e2-b6ad-0fddb3a8565a)
    ![image](https://github.com/docafavarato/linkUp/assets/98183878/369ba064-363d-42c8-a1e3-960e30a3bbce)
    
- ## User interactions
    - ### Posting
        - Users can create, edit and delete their posts.

          ![image](https://github.com/docafavarato/linkUp/assets/98183878/a7847f43-7c9a-4bbb-a99e-b50bd9979959)
          
    - ### Commenting
        - Users can reply to any post, and can also delete their replies.
    - ### Liking
        - Users can like and unlike any post.
    - ### Following
        - Users can follow and unfollow other users, changing the "followers" and "following" amount of their profiles.

          ![image](https://github.com/docafavarato/linkUp/assets/98183878/8b3973ec-b20f-4bf0-93ae-f1955009a23a)

          ![image](https://github.com/docafavarato/linkUp/assets/98183878/7f9b0626-c878-4786-87b9-04298fbb971b)
          
     - ### Searching
    	 - Users are able to search for posts (tags, title, body or content in any of the comments) and other users.

  	   ![image](https://github.com/docafavarato/linkUp/assets/98183878/f6543dad-5e54-4e5e-83bb-a504a4279ad4)
	   ![image](https://github.com/docafavarato/linkUp/assets/98183878/f204785d-0f3d-4411-987c-1498bf2f7de5)
	   ![image](https://github.com/docafavarato/linkUp/assets/98183878/9c4238af-dba0-42fb-89dc-38ab2fb120a5)
           ![image](https://github.com/docafavarato/linkUp/assets/98183878/de30a533-9def-4962-ad01-fef487b699c8)

- ## User profile
    - Each user has a dynamic page based on his ID that displays his profile.
    - The profile pages shows the user infos, such as his name, his profile description, his birth date, his image, his followers/following amount and all the posts that were made by him.
    - Users are able to see all the posts they liked.
      
      ![image](https://github.com/docafavarato/linkUp/assets/98183878/46de5eb2-2cdb-468c-8f38-8a3f069190f9)

    - Users can edit all of their profile informations:

      ![image](https://github.com/docafavarato/linkUp/assets/98183878/c7b909b3-ca61-4e49-8284-78f76024f549)

# Post related
- ## Post structure
    - A post contains an author, a creation date, a title, a body, an image (optional), a list of tags (also optional), a list of comments and a list of users who liked it. Users can show or hide the replies.
      
      ![image](https://github.com/docafavarato/linkUp/assets/98183878/afef68ce-c6d7-47c4-b2a7-2ecd9486d1d9)

    - Users are able to see the exact date that a post was created by hovering over the approximate date:
      
      ![image](https://github.com/docafavarato/linkUp/assets/98183878/24369378-b46f-487a-bbac-948378b46473)

    - Users are able to see everyone that liked a post by hovering over the like amount:

      ![image](https://github.com/docafavarato/linkUp/assets/98183878/e4375b99-0a7e-4d96-89fd-9d12fe00a37d)

# Comment related
- ## Comment structure
  - A comment contains an author, a creation date and a content. Users are able to delete their comments.

    ![image](https://github.com/docafavarato/linkUp/assets/98183878/20b3d776-06f6-4d98-a9c2-6a2e9534544e)

  - Users are able to see the exact date that a comment was made by hovering over the approximate date:

    ![image](https://github.com/docafavarato/linkUp/assets/98183878/dfd46f62-8d02-4c8b-bec9-73f8206069b8)