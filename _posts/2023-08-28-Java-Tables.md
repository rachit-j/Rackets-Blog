---
toc: true
comments: true
layout: post
title: Java Tables
description: This is a collection of data that I have ammassed on topics that I feel familiar with.
type: hacks
courses: { csse: {week: 1}, csp: {week: 1, categories: [4.A]}, csa: {week: 0}, labnotebook: {week: 2} }
categories: [C1.4]
---

### Tables!
The following table is a list of some hotels in Dheli and their reviews. The data comes from [this link](https://www.kaggle.com/datasets/juhibhojani/hotel-reviews).
<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="demo" class="table" border="1" style="background-color:#2E4053; border-radius: 16px; color:#3498DB;">
        <thead>
            <tr>
                <th>Hotel</th>
                <th>Location</th>
                <th>Rating Attribute</th>
                <th>Rating /10</th>
                <th>Review Text</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Hotel The Pearl</td>
                <td>Paharganj, New Delhi</td>
                <td>Best budget friendly hotel</td>
                <td>9</td>
                <td>Hotel the pearl is perfect place to stay in Delhi Paharganj. whole staff are very helpful, informati...</td>
            </tr>
            <tr>
                <td>Hotel City lite Near IGI Airport</td>
                <td>South West, New Delhi</td>
                <td>Exceptional</td>
                <td>10</td>
                <td>The location was good. Easily apporechble.</td>
            </tr>
            <tr>
                <td>New Delhi YMCA Tourist Hostel</td>
                <td>Connaught Place, New Delhi</td>
                <td>Poor cleanliness, poor breakfast, poor service, no water, lock was not working in room...</td>
                <td>5</td>
                <td>Break fast is poor in taste with less varieties. In veg category Idli only available. Location is ve...</td>
            </tr>
            <tr>
                <td>FabHotel Grand Stay</td>
                <td>East Delhi, New Delhi</td>
                <td>Pathetic. Not worth for money.</td>
                <td>1</td>
                <td>Not worth for money. Mosquitoes in the room. Complained to the staff, no proper resolution...</td>
            </tr>
            <tr>
                <td>Delhi Pride Hotel</td>
                <td>Karol bagh, New Delhi</td>
                <td>Exceptional</td>
                <td>10</td>
                <td>Nice hotel good hotel staff Mr Suraj is very good person</td>
            </tr>
            <tr>
                <td>Hotel Neu Villa - Walk In from New Delhi Railway Station</td>
                <td>Paharganj, New Delhi</td>
                <td>Nice stay with good staff</td>
                <td>10</td>
                <td>Location was very premium, staff was super active. The hotel was quite good. The hotel is too close ...</td>
            </tr>
            <tr>
                <td>Hotel City Empire</td>
                <td>Paharganj, New Delhi</td>
                <td>Warm staff and good value of money</td>
                <td>9</td>
                <td>The staff especially Ranjana is warm and caring. She organise the tour for us and ensure each hotel ...</td>
            </tr>
            <tr>
                <td>Hotel Uptown - By Srida Hotels</td>
                <td>Paharganj, New Delhi</td>
                <td>Good</td>
                <td>7</td>
                <td>Good infrastructure and rooms.</td>
            </tr>
            <tr>
                <td>Hotel Lotus Stay At Delhi Airport</td>
                <td>South West, New Delhi</td>
                <td>Very good</td>
                <td>8</td>
                <td>I was stay for one night rooms neat and clean,food was amazing and staff was very good and helpful v...</td>
            </tr>
            <tr>
                <td>Shri Ram Plaza At Delhi Airport</td>
                <td>Mahipalpur, New Delhi</td>
                <td>Exceptional</td>
                <td>10</td>
                <td>Staff members are very co-operative, friendly and helpful. Rooms are as described while booking. Ove...</td>
            </tr>
        </tbody>
    </table>
</body>


<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>

Here is another table coded in markdown about the Oodles of Noodles, ie the annual consumption of noodles per capita. The information is gathered from [here](https://www.statista.com/chart/22865/instant-noodle-consumption-by-country/)

| Country | Servings Per Capita | Total Servings (mill) |
| South Korea | 75.6 | 3900 |
| Nepal | 58.4 | 1640 |
| Indonesia | 46.8 | 12520 |
| Japan | 44.5 | 5630 |
| China | 29.6 | 41450 |
| Australia | 16.8 | 420 |
| Saudi Arabia | 16.6 | 560 |
| US | 14.2 | 4630 |
| UK | 6.3 | 420 |
| India | 5.0 | 6730 |
| France | 1.0 | 70 |
| Argentina | 0.2 | 10 |


### Describe the benefits of a Markdown Table
Markdown tables have a couple benefits. One of them includes their ease of creation. Without large tags and syntax, markdown tables create tables that are equal to HTML tables. Moreover, the editor format is relatively easy to visualize in the actual file, making edits exponentially easier. 

### What is the difference between HTML/CSS Tables and Tables with JavaScript?
Tables with HTML/CSS are static tables; ie the values cannot change and the page does not move. However, with tables with JavaScript can be changed during the webpage, and can impliment other features like searching and scrolling on webpages.

### What are the benefits of a table that uses JavaScript?
A table that uses JavaScript can have flexible rows and columns that can change according to input. This means that the table can change and can be more compact with table scrolling and other features. Moreover, additional API's can be put into the tables, making them even neater and cleaner. 