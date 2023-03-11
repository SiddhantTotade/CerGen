"""This module contains the functions for wrapper-type-casting,
wrapper-type conversions and wrapper-type-testing"""

from typing import TypeVar

T = TypeVar('T', type)

def cast(dst_type: T, obj: object) -> T:
  """Casts or converts a wrapper-object to a type

  The function returns a new wrapper-object of 'dst_type' created for the
  underlying .Net object of the Python object 'obj'. If 'obj' cannot be cast
  to 'dst_type', an error occurs. Unlike the ':func:`as_of`' function, this
  function converts 'obj' to 'dst_type' with respect to  internal methods
  possibly defined in 'dst_type' for explicit conversions between 'dst_type' 
  and the original'obj' type

  :param type dst_type: the target object type.
  :param obj: any wrapper-object.
  :returns: object translated to dst_type."""    
    ...

def as_of(obj: object, dst_type: T) -> T:
  """Reinterprets 'obj' as an object of 'dst_type'
  
  The function returns a new wrapper-object of 'dst_type' created for the
  underlying .Net object of the Python object 'obj'. If 'obj' cannot be cast
  to 'dst_type', an error occurs. Unlike the ':func:`cast`' function, this
  function converts 'obj' to 'dst_type' without regard to internal methods
  possibly defined in 'dst_type' for explicit conversions between 'dst_type'
  and the original type of 'obj'

  :param obj: any wrapper-object.
  :param type dst_type: the target object type.
  :returns: object translated to dst_type."""      
    ...

def is_assignable(obj: object, dst_type: type) -> bool:
  """Returns True if 'obj' can be cast to 'dst_type' with the ':func:`as_of`'
  function, otherwise False"""
      ...

def is_typeof_eq(obj: object, origin_type: type) -> bool:
  """Returns True if the original wrapper-type of the underlying .Net object
  of the Python object 'obj' is 'origin_type' otherwise False"""
    ...

def type_of(ptype: type) -> object:
  """Returns a wrapper-object representing the underlying .Net type for
  a ptype""" 
