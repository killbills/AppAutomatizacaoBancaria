from distutils.core import setup

setup(
    name='Integração Bancária Sienge',
    version='1.0',
    description='App para comunicação com o serviço de automatização bancária do Sienge.',
    author='Team KillBills',
    author_email='g_siengecontasapagar@softplan.com.br',
    url='www.softplan.com.br',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'cefpython',
        'requests',
        'jsonpickle'
    ],
)