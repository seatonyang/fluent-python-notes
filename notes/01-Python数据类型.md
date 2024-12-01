# Python数据类型



初步接触python的小伙伴可能会有疑问，为什么获取一个容器的大小不是使用`collection.len()`，而是使用`len(collection)`？

其实这是典型的python风格，等你熟悉之后你就会发现它非常好用。

python在执行`len(collection)`的时候实际上执行的是`collection.__len__()`方法。可以理解为Python语言提供了自己的API，然后我们平时自己创建类的时候只需要自己实现`class.__len__()`方法，然后就可以使用python的`len()`方法来获取该实例化对象的长度。

类似的`obj[key]`方法调用的是obj对应类的`__getitem__()`方法。 

因此，可以把Python视作一个通用框架，我们只需要自己重写自己类的具体实现逻辑，就可以做到不同类之间都使用`len()`方法来获取该对象的长度。

Python 中有很多以双下划线 `__` 开头和结尾的方法，通常被称为 **魔法方法** 或 **特殊方法**，这些方法提供了对内建操作符或内建函数的自定义支持。除了 `__len__` 以外，还有许多常用的魔法方法可以帮助我们定制类的行为。以下是一些常见的魔法方法：

### 1. **`__init__(self, ...)`**  
- **描述**：类的构造函数，在类实例化时自动调用。
- **用途**：用于初始化对象的状态（如定义属性）。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
  ```

### 2. **`__del__(self)`**  
- **描述**：析构函数，在对象被销毁时自动调用（垃圾回收时）。
- **用途**：清理资源，如关闭文件或数据库连接。
- **示例**：
  ```python
  class MyClass:
      def __del__(self):
          print("Object is being destroyed")
  ```

### 3. **`__repr__(self)`**  
- **描述**：返回对象的“官方”字符串表示，通常用于调试。
- **用途**：当我们调用 `repr()` 或者在交互式解释器中打印对象时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __repr__(self):
          return f"MyClass(value={self.value})"
  ```

### 4. **`__str__(self)`**  
- **描述**：返回对象的“非正式”字符串表示，通常用于 `print()` 函数中。
- **用途**：用于定义对象的友好字符串表示。
- **示例**：
  ```python
  class MyClass:
      def __str__(self):
          return f"MyClass with value {self.value}"
  ```

### 5. **`__add__(self, other)`**  
- **描述**：实现加法运算符 (`+`)。
- **用途**：当对象参与加法操作时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __add__(self, other):
          return MyClass(self.value + other.value)
  ```

### 6. **`__sub__(self, other)`**  
- **描述**：实现减法运算符 (`-`)。
- **用途**：当对象参与减法操作时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __sub__(self, other):
          return MyClass(self.value - other.value)
  ```

### 7. **`__mul__(self, other)`**  
- **描述**：实现乘法运算符 (`*`)。
- **用途**：当对象参与乘法操作时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __mul__(self, other):
          return MyClass(self.value * other.value)
  ```

### 8. **`__getitem__(self, key)`**  
- **描述**：实现索引操作（`[]`）。
- **用途**：当对象使用索引访问时（如 `obj[key]`），调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, items):
          self.items = items
      
      def __getitem__(self, key):
          return self.items[key]
  ```

### 9. **`__setitem__(self, key, value)`**  
- **描述**：实现索引赋值操作（`[] =`）。
- **用途**：当对象使用索引赋值时（如 `obj[key] = value`），调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, items):
          self.items = items
      
      def __setitem__(self, key, value):
          self.items[key] = value
  ```

### 10. **`__delitem__(self, key)`**  
- **描述**：实现删除索引元素操作（`del obj[key]`）。
- **用途**：当使用 `del` 删除对象的索引元素时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, items):
          self.items = items
      
      def __delitem__(self, key):
          del self.items[key]
  ```

### 11. **`__iter__(self)`**  
- **描述**：使对象可迭代，返回一个迭代器对象。
- **用途**：当对象参与迭代（如 `for` 循环）时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, items):
          self.items = items
      
      def __iter__(self):
          return iter(self.items)
  ```

### 12. **`__next__(self)`**  
- **描述**：返回下一个迭代项，配合 `__iter__` 使用。
- **用途**：当对象的迭代器调用 `next()` 时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, items):
          self.items = items
          self.index = 0
      
      def __iter__(self):
          return self
      
      def __next__(self):
          if self.index < len(self.items):
              result = self.items[self.index]
              self.index += 1
              return result
          else:
              raise StopIteration
  ```

### 13. **`__contains__(self, item)`**  
- **描述**：实现 `in` 操作符。
- **用途**：当使用 `item in obj` 时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, items):
          self.items = items
      
      def __contains__(self, item):
          return item in self.items
  ```

### 14. **`__call__(self, ...)`**  
- **描述**：使对象可调用，类似函数调用。
- **用途**：当对象像函数一样被调用时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __call__(self, x):
          return self.value * x
  ```

### 15. **`__eq__(self, other)`**  
- **描述**：实现等于运算符（`==`）。
- **用途**：当使用 `==` 比较两个对象时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __eq__(self, other):
          return self.value == other.value
  ```

### 16. **`__ne__(self, other)`**  
- **描述**：实现不等于运算符（`!=`）。
- **用途**：当使用 `!=` 比较两个对象时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __ne__(self, other):
          return self.value != other.value
  ```

### 17. **`__gt__(self, other)`**  
- **描述**：实现大于运算符（`>`）。
- **用途**：当使用 `>` 比较两个对象时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __gt__(self, other):
          return self.value > other.value
  ```

### 18. **`__lt__(self, other)`**  
- **描述**：实现小于运算符（`<`）。
- **用途**：当使用 `<` 比较两个对象时，调用此方法。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value
      
      def __lt__(self, other):
          return self.value < other.value
  ```

### 19. **`__contains__(self, item)`**  
- **描述**：实现 `in` 运算符，用于检查对象是否包含某个元素。
- **示例**：
  ```python
  class MyClass:
      def __init__(self, items):
          self.items = items
      
      def __contains__(self, item):
          return item in self.items
  ```

### 总结

Python 中的魔法方法使得我们可以重载和定制各种常见操作符和行为，比如对象初始化、迭代、索引访问、运算符重载等。通过实现这些方法，我们可以让自定义类表现得像内建数据类型一样，提供更直观和灵活的接口。

