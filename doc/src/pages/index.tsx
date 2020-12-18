import React from 'react'
import clsx from 'clsx'
import Layout from '@theme/Layout'
import Link from '@docusaurus/Link'
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from './styles.module.css'

export default function MainPage(): JSX.Element {
  const context = useDocusaurusContext()
  const {siteConfig = {}} = context
  return (
    <Layout title='' description={siteConfig.customFields.description}>
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className='container'>
          <h1 className='hero__title'>{siteConfig.title}</h1>
          <p className='hero__subtitle'>{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                'button button--outline button--primary button--mg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/')}
            >
              Get Started
            </Link>
          </div>
        </div>
      </header>
      <main>
        <section className={styles.features}>
          <div className='container'>
            <div className='row'>
              {(() => {
                const title = 'Easy to Use'
                const imageUrl = 'img/undraw_relaunch_day_902d.svg'
                const description = (
                  <>
                    Agraffe was designed to use quickly and to forget on a serverless
                    service.
                  </>
                )

                const img = useBaseUrl(imageUrl)
                return (
                  <div className={clsx('col col--4', styles.feature)}>
                    {img && (
                      <div className='text--center'>
                        <img className={styles.featureImage} src={img} alt={title} />
                      </div>
                    )}
                    <h3>{title}</h3>
                    <p>{description}</p>
                  </div>
                )
              })()}
              {(() => {
                const title = 'Focus on What Matters'
                const imageUrl = 'img/undraw_code_thinking_1jeh.svg'
                const description = (
                  <>
                    Agraffe lets you focus on your API with ASGI. And Agraffe is
                    friendly to{' '}
                    <a
                      href='https://fastapi.tiangolo.com'
                      target='_blank'
                      rel='noopener'
                    >
                      FastAPI
                    </a>
                    , which is fast to code and ready for production.
                  </>
                )
                const img = useBaseUrl(imageUrl)
                return (
                  <div className={clsx('col col--4', styles.feature)}>
                    {img && (
                      <div className='text--center'>
                        <img className={styles.featureImage} src={img} alt={title} />
                      </div>
                    )}
                    <h3>{title}</h3>
                    <p>{description}</p>
                  </div>
                )
              })()}
              {(() => {
                const title = 'Support on Serverless Services'
                const description = (
                  <>
                    Agraffe support on AWS lambda, Google Cloud Functions and Azure
                    Functions.
                  </>
                )

                const imgAWSLambda = useBaseUrl('img/Arch_AWS-Lambda_64.svg')
                const imgCloudFunction = useBaseUrl('img/cloud-functions-512-color.svg')
                const imgAzureFunction = useBaseUrl(
                  'img/10029-icon-service-Function-Apps.svg',
                )
                return (
                  <div className={clsx('col col--4', styles.feature)}>
                    <div className='row'>
                      {imgAWSLambda && (
                        <div className='col col--4'>
                          <img
                            className={styles.featureImage}
                            src={imgAWSLambda}
                            alt='AWSLambda'
                          />
                        </div>
                      )}
                      {imgCloudFunction && (
                        <div className='col col--4'>
                          <img
                            className={styles.featureImage}
                            src={imgCloudFunction}
                            alt='CloudFunction'
                          />
                        </div>
                      )}
                      {imgAzureFunction && (
                        <div className='col col--4'>
                          <img
                            className={styles.featureImage}
                            src={imgAzureFunction}
                            alt='AzureFunction'
                          />
                        </div>
                      )}
                    </div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                  </div>
                )
              })()}
            </div>
          </div>
        </section>
      </main>
    </Layout>
  )
}
