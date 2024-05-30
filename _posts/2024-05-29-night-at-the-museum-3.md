---
toc: True
comments: False
layout: post
title: Tri 3 N@TM Blog
description: Blog for what I saw at N@TM 3
type: hacks
courses: {'csa': {'week': 35}}
---

## Our Project

Our project was to create a game that taught computer science. We had a  great turnout for our project, with many people coming to our booth and a lot of them liking our game. We could have done better with presentation, as some of our group was just sitting down and talking with each other while others were presenting, and then switching off when it was convenient.

## What I saw (images)

<ul>
  {% for image in site.data.files.images %}
    <li>
      <img src="{{ site.baseurl }}/images/tri3natm/{{ image }}" alt="{{ image }}">
    </li>
  {% endfor %}
</ul>

<h2>Videos</h2>
<ul>
  {% for video in site.data.files.videos %}
    <li>
      <video controls>
        <source src="{{ site.baseurl }}/images/tri3natm/{{ video }}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </li>
  {% endfor %}
</ul>
