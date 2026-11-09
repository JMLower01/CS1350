def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            file = open(filename)
            # TODO: Open file
        except FileNotFoundError:
            # TODO: Handle missing file
            print("File not found")
            return file
        except PermissionError:
            print("No permission to access file")
            return file
            # TODO: Handle permission issues
        else:
            return file.read()
            # TODO: Process file content (only if opened successfully)
        finally:
            if file:
                file.close()
            # TODO: Ensure file is closed

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            return self.resource
            # TODO: Implement with possible RuntimeError

        def release(self):
            """Release resource - must always happen."""
            self.resource = None
            # TODO: Implement cleanup

        def use(self):
            """Use resource - only if acquired."""
            print(self.resource)
            # TODO: Implement usage
            pass

    # Test resource management
    rm = ResourceManager("Database")
    try:
        rm.acquire()
    except RuntimeError:
        print("Program timed out")
    else:
        rm.use()
    finally:
        rm.release()
    # TODO: Use try-except-else-finally to manage resource

# Run the practice
practice_3_complete_pattern()


def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""
        # TODO: Add __init__ with position and reason
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason

    class GameOverError(GameError):
        """Game has ended."""
        # TODO: Add __init__ with winner
        def __init__(self, winner):
            self.winner = winner

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):
            if self.game_over:
                raise GameOverError(self.current_player)
            if row > 3 or col > 3:
                raise InvalidMoveError((row, col), "Position out of bounds")
            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "Position taken")
            self.board[row][col] = self.current_player
            
            
            # TODO: Raise GameOverError if game_over is True
            # TODO: Raise InvalidMoveError if position is taken
            # TODO: Raise InvalidMoveError if position is out of bounds
            pass

    # Test the game
    game = TicTacToe()

    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")

# Run the practice
practice_2_custom_exceptions()


def practice_3_complete_system():
    
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)
    # TODO: Build a file processing system with proper error handling
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []
        def process_file(self, filename):
            file = None
            """
            Process a single file with complete error handling.
            """
            # TODO: Implement with try-except-else-finally
            # TODO: Handle FileNotFoundError
            # TODO: Handle PermissionError
            # TODO: Handle general exceptions
            # TODO: Ensure file is closed
            try:
                file = open(filename)
            except FileNotFoundError:
                print("File not found")
                self.failed_files.append(file)
            except PermissionError:
                print("No permission to open file")
                self.failed_files.append(file)
            except Exception:
                print("An error has occured")
                self.failed_files.append(file)
            else:
                file.read()
                self.processed_files.append(file)
            finally:
                if file:
                    file.close()
                    
        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            for file in directory:
                try:
                    self.process_file(file)
                except Exception: 
                    self.failed_files.append(file)
                else: 
                    self.processed_files.append(file)
                
            # TODO: Process each file
            # TODO: Continue on errors
            # TODO: Track successes and failures
            pass
        def get_report(self):
            """
            Get processing report.
            """
            
            report = ""
            report += f"\nProcessed: {len(self.processed_files)}"
            report += f"\nFailed: {len(self.failed_files)}"
            return report
            # TODO: Return summary of processing
            
    # Test the processor
    processor = FileProcessor()
    test_files = [
    "valid.txt",
    "missing.txt",
    "/root/restricted.txt"
    ]
    for filename in test_files:
        processor.process_file(filename)
        
    report = processor.get_report()
    print(f"Report: {report}")
    
# Run the practice
practice_3_complete_system()