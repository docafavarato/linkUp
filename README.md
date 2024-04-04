# <img src="https://i.ibb.co/v4jzr3D/1710963331318.png" width="100"/>

# About
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
 
- A social network with an API built in Java (Spring Boot) and the back/frontend in Python (Flask) and JS/HTML/CSS.

- The API repository is <a href="https://github.com/docafavarato/linkupapi">here</a>

- Author: <a href="https://www.linkedin.com/in/favarato/">João Pedro Favarato</a>

# Features
# User related
- ## User session
  - Session control for different users with Flask's `session` module. Upon login, each user is assigned a unique session identifier.

- ## User login/register
  - When registering, the user information in inserted into the API. When trying to log in, the system verifies the credentials based on the provided email.

    ![image](https://github.com/docafavarato/linkUp/assets/98183878/1fb3f1e0-6701-4673-9961-1b0685339598)
    ![image](https://github.com/docafavarato/linkUp/assets/98183878/9255794a-4367-4ae0-a951-88a9dabbe24b)


- ## User interactions
    - ### Posting
        - Users can create, edit and delete their posts.

          ![image](https://github.com/docafavarato/linkUp/assets/98183878/7ce12039-d1a1-4229-bc81-e6ce673e11d4)

    - ### Commenting
        - Users can reply to any post, and can also delete their replies.
    - ### Liking
        - Users can like and unlike any post.
    - ### Following
        - Users can follow and unfollow other users, changing the "followers" and "following" amount of their profiles.

          ![image](https://github.com/docafavarato/linkUp/assets/98183878/8b3973ec-b20f-4bf0-93ae-f1955009a23a)

          ![image](https://github.com/docafavarato/linkUp/assets/98183878/7f9b0626-c878-4786-87b9-04298fbb971b)

- ## User profile
    - Each user has a dynamic page based on his ID that displays his profile.
    - The profile pages shows the user infos, such as his name, his profile description, his birth date, his image, his followers/following amount and all the posts that were made by him.

      `/profiles/660b286b83c1b05a6290c8f2`
      
      ![image](https://github.com/docafavarato/linkUp/assets/98183878/b65b18b9-246f-433e-94a5-35a253f67c24)
          
# Post related
- ## Post structure
    - A post contains an author, a creation date, a title, a body, a list of comments and a list of users who liked it. Users can show or hide the replies.
      
      ![image](https://github.com/docafavarato/linkUp/assets/98183878/9d54b1f4-b219-4b28-a5c9-86ea102745e2)

    - Users are able to see the exact date that a post was created by hovering over the approximate date:
      
      ![image](https://github.com/docafavarato/linkUp/assets/98183878/e678e122-3a03-44b2-a77f-8ba7b7056ff2)

    - Users are able to see everyone that liked a post by hovering over the like amount:

      ![image](https://github.com/docafavarato/linkUp/assets/98183878/f9255f16-7947-4d3b-a46c-d3e645f0ccb3)

# Comment related
- ## Comment structure
  - A comment contains an author, a creation date and a content. Users are able to delete their comments.

    ![image](https://github.com/docafavarato/linkUp/assets/98183878/ff658467-735e-49bb-9cb0-a775007e41f8)

  - Users are able to see the exact date that a comment was made by hovering over the approximate date:

    ![image](https://github.com/docafavarato/linkUp/assets/98183878/9099038a-91fa-478b-8e67-06a63b14146d)


      

