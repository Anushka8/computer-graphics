import glm


class TransformationStack:
    def __init__(self):
        self.transformation_stack = [glm.mat4(1.0)]

    def push_matrix(self, matrix):
        self.transformation_stack.append(glm.mul(self.get_top(), matrix))

    def get_top(self):
        if self.transformation_stack:
            return self.transformation_stack[-1]
        return glm.mat4(1.0)

    def pop_matrix(self):
        if self.transformation_stack:
            self.transformation_stack.pop()
