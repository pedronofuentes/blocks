# Blocks for Django pages

-----
**Warning**

This is a quite simple way to put pieces of content into a page and reuse it. I know that it will be more robust and powerful solutions to do it. I use it for projects that fits well.

I'm always learning, so any suggestions are welcomed :)
-----

Blocks allows to put some rendered content into a template with tags.

* Define your blocks in your app in blocks.py file.
* The blocks are defined as functions in the file with their name ending with _blocks.
* Blocks should return rendered content for the template.
* You can get blocks with `{% get_block "name" %}` where "name" is the function name with its namespace.

## Example

In your app, in `blocks.py`:

	def foo_block():
		return 'Hello World!'

	def foo_with_argument(arg):
		return 'Hello %s!' % arg

Then you can get this block into the template:

	{% get_block "app.blocks.foo_block" %}

	{% get_block "app.blocks.foo_with_argument" "World"}
