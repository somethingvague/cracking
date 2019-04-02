from nose.tools import assert_true, assert_false
from data_structures.c4_trees_and_graphs.questions.route_between_nodes import path_exists_dfs, path_exists_bfs
from data_structures.c4_trees_and_graphs.structures.graph import Graph


class TestRouteBetweenNodes:
    def setup(self):
        self.b = Graph.Node('b', [])
        self.c = Graph.Node('c', [self.b])
        self.a = Graph.Node('a', [self.b, self.c])
        self.d = Graph.Node('d', [self.a])

    def test_path_exists_dfs_is_true_when_from_and_to_are_equal(self):
        assert_true(path_exists_dfs(self.b, self.b))

    def test_path_exists_dfs_is_true_when_path_exists(self):
        assert_true(path_exists_dfs(self.a, self.b))

    def test_path_exists_dfs_is_false_when_path_does_not_exist(self):
        assert_false(path_exists_dfs(self.a, self.d))

    def test_path_exists_bfs_is_true_when_from_and_to_are_equal(self):
        assert_true(path_exists_bfs(self.b, self.b))

    def test_path_exists_bfs_is_true_when_path_exists(self):
        assert_true(path_exists_bfs(self.a, self.b))

    def test_path_exists_bfs_is_false_when_path_does_not_exist(self):
        assert_false(path_exists_bfs(self.a, self.d))
