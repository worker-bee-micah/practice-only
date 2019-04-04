'''
#Header first level
###### sixth level header
Alt-H1 alt-first level
Alt-H6 alt-first level6
*Italics* are also called * asterisks Emphasis* or _underscoresONends_ .
**Bold** is two asterisks or underscores __before/after__
Nest **underscores within __asterisks__**
Strickthrough uses ~~two~~ two  ~~tildes~~
**Lists**
..*
1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses
..*
..*
**Links**
[This is a basic inline-style link](https://remojo.net)
[Inline with a title](https://remojo.net "Remojo Scientific LLC")

Below is my logo, (hover to see the title text):

Inline-style:
![alt text](https://i.imgur.com/pgqQd7j.jpg "Shrubbery Number One")


Reference-style:
![logo]: https://i.imgur.com/geu1HA1.jpg "Shrubbery Number Five"


**Syntax Highlighting**
Not all renderers will support syntax highlighting.
Inline `code` has `back-ticks around` it.
Multiline code blocks use three back-ticks and the language in lowercase
```python
code_block = "THis is s0m\ne code: that needs work"
print(code_block) if else:
```
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
|Tables          |Are             |Made of Wood   |
|----------------|:--------------:| -------------:|
|column three is |  right-aligned | Liriodendron  |
|column two is   | centered       | Quercus       |
|African Swallows| are neat       | Coconuts      |
|There must be   |three dashes se |parating the   |
|Header. Outer   | Pipes are opt  |ional.         |
|Inline is an    | option also.   |  Semprini     |

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

**Blockquotes**
>Blockquotes are created with a greater than sign in the first column.
>This line should be part of the quote above.

The quote should break here like a killer rabbit.

>This is a super double extra long line that should be entirely within the same blockquote.  I can't believe that you are still reading this instruction manual that I'm writting, way to go champ!

**Inline HTML**
Raw HTML should work also, maybe. Kinda
<dl>
    <dt>Knights of Camelot List</dt>
    <dd>Is not listed here, keep looking.</dd>
    
<dl>
  <dt>Definition lists</dt>
  <dd>Are something E. Henry Thripshaw uses sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

**Horizontal Rule**
Three or more...
---
Hyphens
***
Asterisks or
___
Underscores.

***
___
---

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.

Now you have to answer to the ^bridge ^^keeper.
'''