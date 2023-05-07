# ShelfShare: A Book Sharing Social Network
<img src="https://user-images.githubusercontent.com/111751273/230335373-2b5f43b8-14be-4786-aeac-73b739196a62.jpg" width="100%">

Using the prompt 'Generate a picture of a cozy reading nook with a bookshelf filled with books and a comfortable armchair in warm and inviting colors.' This image was generated using AI on Deep Dream Generator.[^1]

# Criteria A: Planning

## Problem Definition
As a School X book club member, I've observed the absence of a dedicated social network for our book club community. While platforms like Goodreads enable global connections, they don't offer a focused space for our school's book club to share reviews, discussions, or announcements. Users can't edit/delete posts or comments, upload desired images, or view past liked posts. Furthermore, club communication/posting is dispersed across Messenger, Facebook, and Email, making it hard for members to track and stay connected. As there are many different post categories, it is hard to locate specific posts. Consultations with club members (see <a href="https://github.com/jonathanye29/unit4_project#evidence-of-consultation">Evidence of Consultation</a> in Appendix) reveal a clear desire for a dedicated book club social network.

## Success Criteria
1. *[Issue tackled: “ absence of a dedicated social network for our book club community”]* The platform allows only students from School X to register using their school emails.

2. *[Issue tackled: 1. “they don't offer a focused space for our school's book club to share reviews, discussions, or event announcements" 2. "Users can't edit/delete posts or comments”]* Users should be able to post posts of different categories such as: Announcements,  Book Reviews, and Discussions, and be able to edit/delete their posts and comments

3. *[Issue tackled: "club communication/posting is dispersed across Messenger, Facebook, and Email, making it hard for members to track and stay connected"]* The platform should allow users to access all features of the book club in the social network. 

4. *[Issue tackled: "or even see past posts they have liked"]* Users will be able to see all posts they have liked in the past.

5. *[Issue: tackled: “As there are many different post categories, it is hard to locate specific posts.”]* The platform will allow the user to select what kind of posts they would like to view by category.

6. *[Issue tackled: “upload desired images”]* The platform will allow users to upload images in their posts.

## Design Statement
I will design and develop a website for my school’s book club. This website will be developed using HTML, Bootstrap CSS, Python, SQLite, and the Flask framework. It will take approximately 3 weeks to develop and will be evaluated based on the given criteria.


## Rationale for Proposed Solution
There are web and mobile applications; however, mobile apps can only be accessed on mobile devices. Web applications, on the other hand, are accessible on any device with a browser. Therefore,  I will be creating a web application for my school's book club to bring all the necessary features in one place and provide a space for all book club members to connect and engage with each other.

I decided to use HTML to develop the website as it is the standard markup language for creating web pages and web applications. HTML provides a foundation for building the user interface of the social network [^6]. In addition, I have chosen to use Bootstrap CSS, which offers responsiveness and a mobile-first approach, catering to a variety of devices and screen sizes. This combination ensures that the platform will be compatible with various devices and browsers, allowing a wide range of users to access the application with a consistent interface [^7].

Many tools exist for creating web applications, including JavaScript, Python, C++, and more. I've chosen Python for my web application due to its vast library selection [^8], enabling me to meet the book club's large-scale web app needs. I opted for Flask among Python frameworks like Flask because of its flexibility, which is crucial for specialized web apps. Unlike stricter frameworks such as Django, Flask works with numerous tools, allowing me to tailor the social network to the book club's requirements. [^9]

For the website's database, I will be using SQLite. SQLite is a free database that does not require any additional server process, and is implemented on a single file. This database fits my client's needs as it is designed to handle large amounts of data efficiently [^10]. It will be able to store all kinds of information safely and quickly, as it does not require to go through long procedural routines other databases such as IBM db2 use [^11]. SQLite is the best option for the social network as it is reliable, efficient, and cost-friendly.

Word Count: 499


# Criteria B: Design
## System Diagram
![jojojojojojo (1)](https://user-images.githubusercontent.com/111751273/236633366-db243c86-ccdc-41bb-a01c-a45db72f277c.png)
<i>Fig. 2</i> This is the system diagram for the proposed solution

## Flow Diagram
### Login System
![u4flowchart1 (1)](https://user-images.githubusercontent.com/111751273/236664876-93241420-14ad-49cd-94b9-b869e724d9db.png)
<i>Fig. 3</i> This is the flow diagram that details the process of how the login system works.

This handles user login by checking the entered email and password, verifying the password against the stored password in the database, and creating a JWT token upon successful authentication to maintain the user's session. If the login fails, it displays error messages.

## UML Diagram

## ER Diagram
![u4projectERdiagram](https://user-images.githubusercontent.com/111751273/230445149-14e32559-9299-4315-9ded-ff4e93d05c85.jpg)
<i>Fig. </i> Entity-Relationship (ER) diagram for ShelfShare's network database, illustrating the relationships between the Users, Posts, Reviews, and Comments tables. The diagram displays one-to-many relationships using lines starting with '1' and ending with 'N', indicating the cardinality of each relationship. For example, 1 user can have many (n) posts.

![Screen Shot 2023-05-06 at 8 33 21 PM](https://user-images.githubusercontent.com/111751273/236621562-8dc78e4f-7ff3-4a0b-bd85-2984853d328b.png)

<p align="center">
  <i>Fig. </i> Example Data for Users Table (Disclaimer: The data presented is fictional and does not depict real comments or authors)
</p>

<img width="max" alt="Screen Shot 2023-04-07 at 9 28 29 PM" src="https://user-images.githubusercontent.com/111751273/230608878-771dffd3-547a-4f55-9873-fd01c84caaae.png">

<p align="center">
  <i>Fig. </i> Example Data for Posts Table (Disclaimer: The data presented is fictional and does not depict real comments or authors)
</p>

<img width="max" alt="Screen Shot 2023-04-07 at 9 29 29 PM" src="https://user-images.githubusercontent.com/111751273/230608970-0458ea2a-c1e5-49e7-91f8-b46e0da26267.png">

<p align="center">
  <i>Fig. </i> Example Data for Reviews Table (Disclaimer: The data presented is fictional and does not depict real comments or authors) 
</p>
 
<img width="max" alt="Screen Shot 2023-04-07 at 9 29 45 PM" src="https://user-images.githubusercontent.com/111751273/230608999-5e2bdd27-2d98-4099-9478-aab25af60ec6.png">

<p align="center">
  <i>Fig. </i> Example Data for Comments Table (Disclaimer: The data presented is fictional and does not depict real comments or authors)
</p>


## Wireframe
<img width="651" alt="Screen Shot 2023-05-05 at 9 05 47 PM" src="https://user-images.githubusercontent.com/111751273/236453336-e5980aca-6663-4f40-ba87-066a4ca50ca5.png">
<i>Fig. </i> The wireframe diagram displays the layout and structure of the Shelfshare social network application, including the login and registration pages, the homepage, pages for each category, the create post page, and the profile page. Users can navigate between these pages using buttons and links provided on each page. The purpose of the wireframe is to provide a visual representation of the user interface design and the flow of the application.

## Test plan
## Record of Tasks

# Criteria C: Development
## Existing tools
## List of techniques used
## Development

# Criteria D: Functionality


# Works cited
[^1]: “Trending Dreams | Deep Dream Generator.” Deepdreamgenerator.com, 2023, deepdreamgenerator.com/. Accessed 2 Apr. 2023.
[^2]: Grinberg, Miguel. “The Flask Mega-Tutorial Part I: Hello, World!” Miguelgrinberg.com, 2017, blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world. Accessed 3 Apr. 2023.
[^3]: “HTML Tutorial.” W3schools.com, 2023, www.w3schools.com/html/default.asp. Accessed 3 Apr. 2023.
[^4]: Sanyal, Sayantani. 10 Reasons Why Python Is One Of The Best Programming Languages. Accessed 7 Apr. 2023
[^5]: “Flask.” Fullstackpython.com, 2016, www.fullstackpython.com/flask.html. Accessed 7 Apr. 2023.
[^6]: “Advantages and Disadvantages of HTML.” GeeksforGeeks, GeeksforGeeks, 25 Oct. 2020, www.geeksforgeeks.org/advantages-and-disadvanatges-of-html/. Accessed 10 April 2023.
[^7]: Cyber Success. “What Is Bootstrap & Advantages of Bootstrap in Web Development.” Cyber Success, 24 Oct. 2021, www.cybersuccess.biz/advantages-of-bootstrap/. Accessed 10 April 2023.
[^8]: Advantages and disadvantages of python - how it is dominating Programming World. DataFlair. Accessed April 10, 2023
[^9]: Simplilearn. “Django vs. Flask: Understanding the Major Differences.” Simplilearn.com, Simplilearn, 4 Feb. 2021, www.simplilearn.com/flask-vs-django-article#:~:text=Flask%20provides%20complete%20control%20and,best%20for%20developing%20sophisticated%20applications. Accessed 10 April 2023.
[^10]: Gomathy, Kavya. "5 Reasons to Use SQLite, the Tiny Giant for Your Next Project." Medium, The Startup, 4 Jan. 2022, https://medium.com/swlh/5-reasons-to-use-sqlite-the-tiny-giant-for-your-next-project-a6bc384b2df4. Accessed April 10, 2023
[^11]: Yegulalp, Serdar. "Why You Should Use SQLite." InfoWorld, IDG Communications, Inc., 13 Feb. 2019, https://www.infoworld.com/article/3331923/why-you-should-use-sqlite.html. Accessed April 10, 2023
[^12]: Otto, Mark. “Get Started with Bootstrap.” Getbootstrap.com, 2023, getbootstrap.com/docs/5.3/getting-started/introduction/. Accessed 26 Apr. 2023.
[^13]:lipis. “Lipis/Flag-Icons: A Curated Collection of All Country Flags in SVG — plus the CSS for Easier Integration.” GitHub, 28 Mar. 2023, github.com/lipis/flag-icons. Accessed 23 Apr. 2023.

‌


# Appendix

## Evidence of Consultation
![Screen Shot 2023-05-06 at 8 46 37 PM](https://user-images.githubusercontent.com/111751273/236622106-71c778b6-838a-4e12-ac89-4bdc96d31c0d.png)
<i>Fig. </i> (Messenger names kept confidential for privacy purposes)


