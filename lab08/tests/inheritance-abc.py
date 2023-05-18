test = {
  'name': 'Inheritance ABCs',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A:
          ...   x, y = 0, 0
          ...   def __init__(self):
          ...         return
          >>> class B(A):
          ...   def __init__(self):
          ...         return
          >>> class C(A):
          ...   def __init__(self):
          ...         return
          >>> print(A.x, B.x, C.x)
          0f757651e6a60891c18d27d3928137af
          # locked
          >>> B.x = 2
          >>> print(A.x, B.x, C.x)
          9691539051f7ce8ef1d33540b01edf6f
          # locked
          >>> A.x += 1
          >>> print(A.x, B.x, C.x)
          ac2ca309cd657a342d1cc0db594a98bb
          # locked
          >>> obj = C()
          >>> obj.y = 1
          >>> C.y == obj.y
          9b87ee740b72a262114634ab6b9e401e
          # locked
          >>> A.y = obj.y
          >>> print(A.y, B.y, C.y, obj.y)
          97fac195808d5eb8632743702830391d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
