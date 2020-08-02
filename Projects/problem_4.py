class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    else:
        for g in group.get_groups():
            if is_user_in_group(user, g):
                return True

    return False


def test():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group("sub_child_user", child))


def test1():
    parent = Group("parent")
    print(len(parent.groups) == 0)


def test2():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    sub_child_user1 = "sub_child_user1"
    sub_child.add_user(sub_child_user1)

    sub_child_user2 = "sub_child_user2"
    sub_child.add_user(sub_child_user2)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group("sub_child_user1", parent))

test2()
test1()