# Auto-Quest

jRPG-style combat framework

Decoupled into battle and character interfaces

## `Battle`

The battle interface provides an execution and logging structure around character actions. `Battles` need to implement the following:

```python
class Battle:
    def group(self, characters):

    def sort(self, characters):

    def done(self, characters):
```


## `Character`

The character interface provides high-level interaction methods used by `Battle`. `Characters` need to implement the following:

```python
class Character:
  def id(self):

  def priority(self):

  def status(self):

  def snapshot(self):

  def act(self, characters, affiliation):
```
