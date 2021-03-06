import torch


def squash(inputs, axis=-1):
    """
    Do squashing
    :param inputs (tensor): tensor of dim [M, num_capsules, capsule_dim]
    :param axis: the dim to apply squash
    :return:
        (tensor): squashed tensor of dim [M, num_capsules, capsule_dim]
    """
    norm = torch.norm(inputs, p=2, dim=axis, keepdim=True)
    scale = norm ** 2 / (1 + norm ** 2) / (norm + 1e-8)
    return scale * inputs

