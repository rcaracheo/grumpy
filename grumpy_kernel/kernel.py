import random
import base64
from ipykernel.kernelbase import Kernel

class GrumpyKernel(Kernel):
    implementation = 'Grumpy'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "Grumpy kernel - positive and constructive feedback for your code"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if code.strip().lower().startswith('hey'):
                msg = "oh, you again... \U0001F64D"
            elif code.startswith('<?'):
                msg = "PHP in 2018? Yeah, more trending than Blockchain!"
            elif '<-' in code:
                msg = '\U0001F4A9 <- how you make me feel'
            elif code.startswith('10 '):
                msg = 'In your language: 20 GOTO HELL'
            elif code.startswith('print '):
                msg = 'every time you use Python 2, God kills a core developer...'
            elif code.startswith('print('):
                msg = '\U00002764'
            elif 'linspace' in code:
                msg = 'Do you want to pay £1,800 for software worse than numpy?\n'
                msg += '\t1) No\n'
                msg += '\t2) Never\n'
                msg += '\t3) Are you kidding?'
            else:
                msg = random.choice([
                    'whatever...',
                    "why don't you look for a hobby?",
                    "it's not you, it's me...",
                ])

            stream_content = {'name': 'stdout', 'text': msg}
            '''
            with open('/home/mgarcia/src/grumpy/grumpy_kernel/grumpy_cat.jpeg', 'rb') as f:
                stream_content = {'name': 'stdout', 'data': {'image/jpeg': base64.b64encode(f.read())}}
            '''
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
