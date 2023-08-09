from scipy.spatial import ConvexHull
import numpy as np

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[0] - p3[1])

def check_triangle_conv_approach(f_p, s_p, t_p, new_point):
    """
    check if the new point lies inside the triangle formed by the first three points
    """
    conv = ConvexHull([f_p, s_p, t_p, new_point], qhull_options='QbB')
    if conv.points != 3:
        return False
    else:
        return True

def check_triangle_sign_2Dapproach(p1,p2,p3,new_point):
    """ 
        each turn in for v1v2 v2v3 and v3v1 must be a right turn, which is positive or negative
        that means we want to check that all the turns are either all positive or all of them are negative 
             v2
            / \
           /   \
          /  v0 \
         /_______\
        v1        v3
    """
    eps = 1e-13
    d1 = sign(p1,p2,new_point)
    d2 = sign(p2,p3,new_point)
    d3 = sign(p3,p1,new_point)

    has_neg = d1 < eps or d2 < eps or d3 < eps
    has_pos = d1 > eps or d2 > eps or d3 > eps
    return not (has_neg and has_pos)


def is_point_inside_triangle_3D_baryacentric(a,b,c, point):
    # triangle_vertices should be a list of three 3D points representing the triangle's vertices.
    # point is the 3D point that you want to check if it's inside the triangle.

    def compute_barycentric_weights(p, a, b, c):
        v0 = b - a
        v1 = c - a
        v2 = p - a

        d00 = v0.dot(v0)
        d01 = v0.dot(v1)
        d11 = v1.dot(v1)
        d20 = v2.dot(v0)
        d21 = v2.dot(v1)

        denominator = d00 * d11 - d01 * d01
        beta = (d11 * d20 - d01 * d21) / denominator
        gamma = (d00 * d21 - d01 * d20) / denominator
        alpha = 1.0 - beta - gamma

        return alpha, beta, gamma

    alpha, beta, gamma = compute_barycentric_weights(point, a, b, c)

    # Check if the point is inside the triangle (Barycentric coordinates are between 0 and 1, and their sum is 1).
    return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1 and abs(alpha + beta + gamma - 1.0) <= 1e-6


def complete_convex(convexhull: ConvexHull):
    # get facets
    facets = convexhull.simplices
    # get points
    points = convexhull.points

    # get triangle points
    facets_points = points[facets]
    
    # get base vectors of the triangle 
    first_vectors = facets_points[:,1] - facets_points[:, 0]
    
    second_vectors = facets_points[:,2] - facets_points[:, 0]
    
    # get more triangle points
    more_points = []

    # iterate from the second point in 1/n of a step
    n = 16
    k = 16
    for i in range(1,n,1):
        # move the vector to where the first point is, and scale it by i/n of the vector
        width_line_points = first_vectors * (i/n) + facets_points[:,0]

        for j in range(1,k,1):
            # add the second vector scaled from where the vector landed
            depth_line_points = second_vectors * (j/k) + width_line_points

            # filter array, i.e select only the points which fall on the facets
            for ind in range(len(depth_line_points)):
                new_point = depth_line_points[ind]

                if is_point_inside_triangle_3D_baryacentric(facets_points[ind,0], 
                                                facets_points[ind,1], 
                                                facets_points[ind,2], new_point):
                    more_points.append(new_point)
    
    return np.concatenate([convexhull.points, np.array(more_points)], axis=0)


