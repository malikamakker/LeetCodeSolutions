class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        for c in expression:
            if c != '}':
                stack.append(c)
            else:
                current_list = ['']
                while len(stack):
                    popped = stack.pop()

                    if popped == '{':
                        stack.append(current_list)
                        break

                    if popped == ',':
                        current_list.insert(0, '')
                        continue

                    current_list[0] = self.perform_union(popped, current_list[0])

        current_list = ['']

        # one more round to review commas
        while (len(stack)):
            popped = stack.pop()

            if popped == ',':
                current_list.insert(0, '')
                continue

            current_list[0] = self.perform_union(popped, current_list[0])
        stack.append(current_list)

        current_list = ['']

        while (len(stack)):
            current_list = self.perform_union(stack.pop(), current_list)

        current_list = set(current_list)
        return list(sorted(current_list))

    def perform_union(self, a, b):
        final = []
        if not isinstance(a, list):
            a = [a]
        if not isinstance(b, list):
            b = [b]
        for x in a:
            for y in b:
                if isinstance(x, list) or isinstance(y, list):
                    final = final + (self.perform_union(x, y))
                else:
                    final.append(x + y)
        return final
