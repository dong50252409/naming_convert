# naming_convert
Convert variable naming style between underscore, camelCase and dot notation

## Installation

.. code-block:: bash
  pip install naming_convert


## Usage

.. code-block:: python
  from naming_convert import *
  
  # convert underscore to camelCase
  to_camel_case('hello_world') # Output helloWorld
  
  # convert underscore to PascalCase
  to_pascal_case('hello_world') # Output HelloWorld
  
  # convert underscore to dot notation
  to_dot_notation('hello_world') # Output hello.world
  
  # convert underscore to screaming snake case
  to_screaming_snake_case('hello_world') # Output HELLO_WORLD
  
  # convert underscore to kebab case
  to_kebab_case('hello_world') # Output hello-world
  
  # convert underscore to screaming kebab case
  to_screaming_kebab_case('hello_world') # Output HELLO-WORLD
  
  # convert underscore to train case
  to_train_case('hello_world') # Output Hello-World
  
  # convert underscore to title case
  to_title_case('hello_world') # Output Hello World
