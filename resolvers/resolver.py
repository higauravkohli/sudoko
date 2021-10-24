import domain.sudoku as Sudoku
import abc

class Resolver(metaclass=abc.ABCMeta):
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'resolve') and 
                callable(subclass.resolve))

    @abc.abstractmethod
    def resolve(s: Sudoku) -> bool:
        """resolve zero placeholders with digit options"""
        raise NotImplementedError
