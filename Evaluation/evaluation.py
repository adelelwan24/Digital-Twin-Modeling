from scipy.spatial import cKDTree

import numpy as np
from scipy.spatial import cKDTree
import trimesh


class Evaluater:
    def __init__(self):
        pass

    def normalize_vertices(self, vertices):
        """
        function to normalize vertices
        :param vertices: vertices
        :return: normalized vertices
        """
        min_val = np.min(vertices, axis=0)
        max_val = np.max(vertices, axis=0)
        normalized_vertices = (vertices - min_val) / (max_val - min_val)
        return normalized_vertices
    

    def get_curvature(self, mesh):
        """
        function to calculate curvature of a mesh
        :param mesh: mesh
        :return: curvature
        """
        curvature = trimesh.curvature.discrete_mean_curvature_measure(mesh)
        return curvature
    
    def eval3d_chamfer_distance(self, actual_vertices: np.ndarray, pred_vertices: np.ndarray, normalized: bool = True) -> float:
        """
        function to calculate chamfer distance between actual and predicted vertices, normalize before calculating
        :param actual_vertices: actual vertices
        :param pred_vertices: predicted vertices
        :return: chamfer distance
        """
        if normalized:
            actual_vertices = self.normalize_vertices(actual_vertices)
            pred_vertices = self.normalize_vertices(pred_vertices)
        actual_tree = cKDTree(actual_vertices)
        pred_tree = cKDTree(pred_vertices)
        dist1, _ = actual_tree.query(pred_vertices)
        dist2, _ = pred_tree.query(actual_vertices)
        chamfer_distance = np.mean(dist1) + np.mean(dist2)
        return chamfer_distance
    


    def eval3d_feature_similarity(self, actual_mesh:trimesh.base.Trimesh, pred_mesh:trimesh.base.Trimesh, normalized: bool = True) -> float:
        """
        function to calculate feature similarity between actual and predicted meshes
        :param actual_mesh: actual mesh
        :param pred_mesh: predicted mesh
        :param normalized: normalize before calculating, default True
        :return: feature similarity
        """
        actual_curvature = self.get_curvature(actual_mesh)
        pred_curvature = self.get_curvature(pred_mesh)
        if normalized:
            min_len = min(len(actual_curvature), len(pred_curvature))
            actual_curvature = actual_curvature[:min_len]
            pred_curvature = pred_curvature[:min_len]

        feature_similarity = np.mean(np.abs(actual_curvature - pred_curvature))
        return feature_similarity
