from unittest import TestCase
from pylinkedmap import LinkedMap

class TestLM(TestCase):
    def test_start(self):
        l = LinkedMap()
        self.assertEqual(len(l), 0)

        l['one'] = 10
        self.assertEqual(len(l), 1)

    def test_get(self):

        l = LinkedMap()
        self.assertEqual(len(l), 0)

        l['one'] = 10
        self.assertEqual(len(l), 1)

        self.assertEqual(l['one'], 10)


    def test_iter(self):

        l = LinkedMap()

        items = [['one', 10], ['two', 20], ['three',30]]

        for elem in items:
            l[elem[0]] = elem[1]
        
        res = zip([x for x in l], items)
        self.assertTrue(all([x[0][0] == x[1][0] and
                             x[0][1] == x[1][1]
                             for x
                             in res]))

    def test_iter_reverse(self):
        l = LinkedMap()

        items = [['one', 10], ['two', 20], ['three',30]]

        for elem in items:
            l[elem[0]] = elem[1]

        res = zip(reversed(l), reversed(items))
        print([x for x in res])
        self.assertTrue(all([x[0][0] == x[1][0] and
                             x[0][1] == x[1][1]
                             for x
                             in res]))

    def test_delete(self):
        l = LinkedMap()
        items = [['one', 10], ['two', 20], ['three',30]]

        for elem in items:
            l[elem[0]] = elem[1]

        del l['two']
        self.assertEqual(len(l), 2)

        res = zip([x for x in l], [x for x in items if x[0] != 'two'])
        self.assertTrue(all([x[0][0] == x[1][0] and
                             x[0][1] == x[1][1]
                             for x
                             in res]))

    def test_next_for(self):

        l = LinkedMap()
        items = [['one', 10], ['two', 20], ['three',30]]

        for elem in items:
            l[elem[0]] = elem[1]
        
        self.assertEqual(l.next_for('two'), 'three')

    def test_prev_for(self):
        
        l = LinkedMap()
        items = [['one', 10], ['two', 20], ['three',30]]

        for elem in items:
            l[elem[0]] = elem[1]
        
        self.assertEqual(l.next_for('two'), 'three')        

    def test_first_last(self):
        
        l = LinkedMap()
        items = [['one', 10], ['two', 20], ['three',30]]

        for elem in items:
            l[elem[0]] = elem[1]
        
        self.assertEqual(l.first(), ('one',10))
        self.assertEqual(l.last(), ('three',30))

    def test_clear(self):
        l = LinkedMap()
        items = [['one', 10], ['two', 20], ['three',30]]

        for elem in items:
            l[elem[0]] = elem[1]

        self.assertEqual(len(l), 3)            
        l.clear()
        self.assertEqual(len(l), 0)

    def test_from_list(self):
        l = LinkedMap([['one', 10], ['two', 20], ['three',30]])
        self.assertEqual(len(l), 3)

        
        
