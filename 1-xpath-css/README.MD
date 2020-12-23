### Selectors
`//elementName[@attribute='value']`
`//elementName[@id='value']`
`//elementName0@class='value']`

### Position
```
Ul
  li      //li[1]
  li      //li[position() = 1 or position() = 2]
  li      //li[position() = 1 and contains(@text, 'hello')]
```

### starts-with(), contains(), ends-with()

### //elementName[predicate]

### Axes
`axisName::elementName`

<table>
  <tr>
    <td>Going UP</td>
    <td>Going DOWN</td>
  </tr>
  <tr>
    <td>
      parent: `//p[@id='outside']/parent::node()`<br>
      ancestor: `/p[@id='outside']/ancestor::node()`<br>
      preceding: excluding its ancestors<br>
      preceding-sibling
    </td>
    <td>
      child: return children<br>
      following: all the elements that are after the closing tag<br>
      following-sebling: return all the elements after the closing tag but should the same parent<br>
      descendant: return the descendants
    </td>
  </tr>
</table>