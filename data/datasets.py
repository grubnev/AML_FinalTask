import torchvision.datasets as datasets

# Загрузка датасета CIFAR-10
cifar10_train = datasets.CIFAR10(root='./data', train=True, download=True, transform=None)
cifar10_test = datasets.CIFAR10(root='./data', train=False, download=True, transform=None)

# Загрузка датасета CIFAR-100
cifar100_train = datasets.CIFAR100(root='./data', train=True, download=True, transform=None)
cifar100_test = datasets.CIFAR100(root='./data', train=False, download=True, transform=None)


print("CIFAR-10 train dataset length:", len(cifar10_train))
print("CIFAR-10 test dataset length:", len(cifar10_test))
print("CIFAR-100 train dataset length:", len(cifar100_train))
print("CIFAR-100 test dataset length:", len(cifar100_test))
