---
title: 'Vim Cut, Copy, and Past'
description: ''
date: 2024-10-13T9:30:00+09:00
lastmod: 
draft: false
---

## Whole Line Operation

* ``yy`` or `Shift + Y`: Yank (copy) the current line
* ``dd``: Delete (cut) the current line
* ``p``: Paste the yanked or deleted text after the current line on the cursor
* ``Shift + p``: Paste the yanked or deleted text before the current line on the the cursor

## Partial Operation

1. Move the cursor to the start point of the sentence that you want yank or delete
2. Press ``v`` to enter visual mode. You will see ``-- Visual --`` in the lower left corner of the terminal (Press ``Esc`` if you want cancel)
3. Move the cursor to the end point of the sentence that you want yank or delete (Selected part will be highlighted)
4. Press ``y`` for yank (copy) or ``d`` for delete (cut)
5. Move the cursor and press ``p`` to past it to the next line or ``Shift + p`` for up line
